#import maya.mel as mel
import maya.cmds as cmds
import random as rnd

# ------------------ UI ----------------------
MyWin = 'Lego Blocks'
if cmds.window( MyWin, exists = True ):
    cmds.deleteUI( MyWin, window = True )

# menu shelf buttons
MyWin = cmds.window( MyWin, menuBar=True, widthHeight = (500,800) )
cmds.menu( label = "Basic Options" )
cmds.menuItem( label = "New Scene", command = ( 'cmds.file( new = True, force = True )' ) )
cmds.menuItem( label = "Delete Scene", command = ( 'cmds.delete()' ) )

# normal blocks
# columns and sliders and whatnot
cmds.frameLayout( collapsable = True, label = "Standard Block", width = 475, height = 180 )

cmds.columnLayout()
cmds.intSliderGrp( 'blockHeight', l = "Height", f = True, min = 1, max = 20, value = 3 )
cmds.intSliderGrp( 'blockWidth', l = "Width (Bumps)", f = True, min = 1, max = 20, value = 2 )
cmds.intSliderGrp( 'blockDepth', l = "Depth (Bumps)", f = True, min = 1, max = 20, value = 8 )
# color slider
# hsv more intuitive, but can extract later as rgb
cmds.colorSliderGrp( 'blockColor', label = "Colour", hsv = (120, 1, 1) )
# slider to make a bunch of normal blocks
cmds.intSliderGrp( 'numBlocks', l = "Number of blocks", f = True, min = 1, max = 100, value = 1 )

cmds.columnLayout()
cmds.button( label = "Create Basic Block", command = ('basicBlock()') )
cmds.button( label = "Create Blocks", command = ('moreBlocks()') )
cmds.setParent( '..' )

cmds.setParent( '..' ) # sliders column layout
cmds.setParent( '..' ) # entire thing

# sloped blocks
cmds.frameLayout( collapsable = True, label = "Sloped Block", width = 475, height = 160 )
cmds.columnLayout()

cmds.intSliderGrp( 'slopedWidth', l = "Width (Bumps)", f = True, min = 1, max = 20, value = 4 )
cmds.intSliderGrp( 'slopedDepth', l = "Depth (Bumps)", f = True, min = 2, max = 4, value = 2 )
cmds.colorSliderGrp( 'slopedColor', label = "Colour", hsv = (120, 1, 1) )

cmds.columnLayout()
cmds.button( label = "Create Sloped Block", command = ('slopedBlock()') )
cmds.setParent( '..' )

cmds.setParent( '..' ) # sliders column layout
cmds.setParent( '..' ) # entire thing

# misc blocks
cmds.frameLayout( collapsable = True, label = "Custom Block", width = 475, height = 160 )
cmds.columnLayout()

# you can choose what type of block, number of blocks, and color
# type of block is associated with a number
cmds.intSliderGrp( 'blockType', l = "Block Type", f = True, min = 1, max = 20, value = 1 )
cmds.intSliderGrp( 'numMisc', l = "Number of blocks", f = True, min = 1, max = 100, value = 1 )
cmds.colorSliderGrp( 'miscColor', label = "Colour", hsv = (120, 1, 1) )

cmds.columnLayout()
cmds.button( label = "Create Custom Block", command = ('customBlock()') )
cmds.setParent( '..' )

cmds.setParent( '..' ) # sliders column layout
cmds.setParent( '..' ) # entire thing

cmds.showWindow( MyWin )

# ------------------------- FUNCTIONS --------------------
# makes individual block with cylinder on top, amt made is based on inputs
# then combines them after; only works for basic rectangle blocks
def basicBlock():
    # grabbing values
    blockHeight = cmds.intSliderGrp( 'blockHeight', q = True, v = True )
    blockWidth = cmds.intSliderGrp( 'blockWidth', q = True, v = True )
    blockDepth = cmds.intSliderGrp( 'blockDepth', q = True, v = True )
    rgb = cmds.colorSliderGrp( 'blockColor', q = True, rgbValue = True )

    #create namespace for blocks on creation so names + numbers stay consistent
    nsTmp = "Block" + str( rnd.randint( 1000, 9999 ))
    cmds.select( clear = True )
    cmds.namespace( add = nsTmp ) # create namespace
    cmds.namespace( set = nsTmp ) # move into namespace

    # scaling block sizes from human numbers to computer numbers
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32

    cmds.polyCube( h = cubeSizeY, w = cubeSizeX, d = cubeSizeZ )
    cmds.move((cubeSizeY / 2.0), moveY = True )

    # creating bumps on block
    for i in range( blockWidth ):
        for j in range( blockDepth ):
            cmds.polyCylinder( r = 0.25, h = 0.20 )
            cmds.move(( cubeSizeY + 0.10 ), moveY = True, a = True )
            cmds.move((( i * 0.8 ) - ( cubeSizeX / 2.0 ) + 0.4 ), moveX = True, a = True )
            cmds.move((( j * 0.8 ) - ( cubeSizeZ / 2.0 ) + 0.4 ), moveZ = True, a = True )
    
    myShader = cmds.shadingNode( 'lambert', asShader = True, name = "blockMat" )
    cmds.setAttr( nsTmp + ":blockMat.color", rgb[0], rgb[1], rgb[2], type = 'double3' )

    cmds.polyUnite(( nsTmp + ":*"), n = nsTmp, ch = False )
    cmds.delete( ch = True ) # delete history

    # assigning mat to block
    cmds.hyperShade( assign = ( nsTmp+":blockMat" ))
    # i guess no need for namespace?
    cmds.namespace( removeNamespace = ":" + nsTmp, mergeNamespaceWithParent = True )

    #cmds.namespace( set = ":" ) # get out of namespace

# creates several basic blocks based on input
def moreBlocks():
    numBlock = cmds.intSliderGrp( 'numBlocks', q = True, v = True )

    # create this many blocks
    for i in range( numBlock ):
        basicBlock()

# creates blocks with a slope, they have more constraints
def slopedBlock():
    blockHeight = 3
    blockWidth = cmds.intSliderGrp( 'slopedWidth', q = True, v = True )
    blockDepth = cmds.intSliderGrp( 'slopedDepth', q = True, v = True )
    rgb = cmds.colorSliderGrp( 'slopedColor', q = True, rgbValue = True )

    nsTmp = "Block" + str( rnd.randint( 1000, 9999 ))
    cmds.select( clear = True )
    cmds.namespace( add = nsTmp ) # create namespace
    cmds.namespace( set = nsTmp ) # move into namespace

    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32

    # making cube with subdiv on width
    cmds.polyCube( h = cubeSizeY, w = cubeSizeX, d = cubeSizeZ, sz = blockDepth )
    cmds.move((cubeSizeY / 2.0), moveY = True )

    # bumps
    for i in range( blockWidth ):
        cmds.polyCylinder( r = 0.25, h = 0.20 )
        cmds.move(( cubeSizeY + 0.10 ), moveY = True, a = True )
        cmds.move((( i * 0.8 ) - ( cubeSizeX / 2.0 ) + 0.4 ), moveX = True, a = True )
        cmds.move(( 0 - ( cubeSizeZ / 2.0 ) + 0.4 ), moveZ = True )

    # material
    myShader = cmds.shadingNode( 'lambert', asShader = True, name = "blockMat" )
    cmds.setAttr( nsTmp + ":blockMat.color", rgb[0], rgb[1], rgb[2], type = 'double3' )
    cmds.polyUnite(( nsTmp + ":*"), n = nsTmp, ch = False )
    cmds.delete( ch = True ) # delete history
    cmds.hyperShade( assign = ( nsTmp+":blockMat" ))

    # slope
    cmds.select(( nsTmp + ":" + nsTmp + ".e[1]" ), r = True)
    cmds.move( 0, -0.8, 0, r = True )

    # 4 block has a special thing so it goes first
    if blockDepth == 4:
        # locating a vertex/ common point to converge to
        tV = cmds.xform(( nsTmp + ":" + nsTmp + ".vtx[8]" ), q = True, t = True)
        cmds.select(( nsTmp + ":" + nsTmp + ".vtx[6]" ), r = True)
        cmds.move( tV[0], tV[1], tV[2], a = True )

    if blockDepth >= 3:
        tV = cmds.xform(( nsTmp + ":" + nsTmp + ".vtx[6]" ), q = True, t = True)
        cmds.select(( nsTmp + ":" + nsTmp + ".vtx[4]" ), r = True)
        cmds.move( tV[0], tV[1], tV[2], a = True )

        tV = cmds.xform(( nsTmp + ":" + nsTmp + ".vtx[7]" ), q = True, t = True)
        cmds.select(( nsTmp + ":" + nsTmp + ".vtx[5]" ), r = True)
        cmds.move( tV[0], tV[1], tV[2], a = True )

    cmds.namespace( removeNamespace = ":" + nsTmp, mergeNamespaceWithParent = True )

# trying to create a type of block based on input so we don't have a bajillion buttons
# bear with me, python doesnt have proper switch case and idk what version of python this is
def customBlock():
    # create x type of block
    blockType = cmds.intSliderGrp( 'blockType', q = True, v = True ) 
    numBlock = cmds.intSliderGrp( 'numMisc', q = True, v = True )
    rgb = cmds.colorSliderGrp( 'miscColor', q = True, rgbValue = True )
    if (blockType == 1):
        singleStud() # 2x2 plate with stud in center
    elif (blockType == 2):
        manWhat()
    elif (blockType == 3):
        noWay()

    # TODO: create this many blocks
    # TODO: make them in this color
    

# creates a 2x2 plate with stud in middle
# might have to clean up
def singleStud():
    cmds.polyCube( h = 0.32, w = 1.6, d = 1.6, n = 'plate' )
    cmds.polyCylinder( r = 0.3, h = 0.32, n = 'outCyl' )
    cmds.polyCylinder( r = 0.2, h = 0.32, n = 'innCyl' )
    cmds.polyBoolOp( 'outCyl', 'innCyl', op=2, n='stud' )
    cmds.move( 0, 0.16, 0, 'stud' )
    cmds.polyBoolOp( 'plate', 'stud', op=1 )
    cmds.delete( ch = True )

def manWhat():
    print("printing man What")

def noWay():
    print("printing no way")