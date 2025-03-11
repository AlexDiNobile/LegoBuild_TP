import maya.cmds as cmds
import random as rnd

#Building the GUI for the Lego Blocks
MyWin = 'Lego Blocks'
if cmds.window(MyWin, exists=True):
    cmds.deleteUI(MyWin, window=True)
    
MyWin = cmds.window(MyWin, menuBar=True, widthHeight=(500, 800))

cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", command=('cmds.file(new=True, force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))

#creating the settings for a standard sized lego brick
cmds.frameLayout(collapsable=True, label="Standard Block", width=475, height=140)

cmds.columnLayout()

#Size Settings
cmds.intSliderGrp('blockHeight',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', l="Width (Bumps)", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('blockDepth', l="Depth (Bumps)", f=True, min=1, max=20, value=8)

#Colour Settings
cmds.colorSliderGrp('blockColour', label="Colour", hsv=(120, 1, 1))

#Modifer Settings (Adding a side stud and making a hole in the size)
cmds.checkBox ('addSideStud', l='Add Hollow Side Stud', v=0)
cmds.checkBox ('makeSideHole', l='Make Side Hole', v=0)
cmds.checkBox ('makeMultSideHoles', l='Make Multiple Side Holes', v=0)
cmds.checkBox ('makeArch', l='Make Arch', v=0)
cmds.checkBox ('makeTopStudsHollow', l='Make Top Studs Hollow', v=0)
cmds.checkBox ('makeAxleHole', l='Make Axle Hole', v=0)

cmds.columnLayout()

#create brick
cmds.button(label="Create Basic Block", command=('basicBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#creating the settings for a Tile brick
cmds.frameLayout(collapsable=True, label="Tile Block", width=475, height=140)

cmds.columnLayout()

#Size Settings
cmds.intSliderGrp('tileBlockHeight',l="Height", f=True, min=1, max=1, value=1)
cmds.intSliderGrp('tileBlockWidth', l="Width", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('tileBlockDepth', l="Depth", f=True, min=1, max=20, value=8)

#Colour Settings
cmds.colorSliderGrp('tileBlockColour', label="Colour", hsv=(120, 1, 1))

#modifer Settings (Add central stud to tile)
cmds.checkBox ('addTileCentralStud', l='Add Hollow Central Stud', v=0)
cmds.columnLayout()

#create brick
cmds.button(label="Create Tile Block", command=('tileBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#creating the settings for a corner lego brick
cmds.frameLayout(collapsable=True, label="Corner Block", width=475, height=140)

cmds.columnLayout()

#Size Settings
cmds.intSliderGrp('cornerBlockHeight',l="Height", f=True, min=1, max=20, value=1)

#Colour Settings
cmds.colorSliderGrp('cornerBlockColour', label="Colour", hsv=(120, 1, 1))
cmds.columnLayout()

#create brick
cmds.button(label="Create Corner Block", command=('cornerBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#creating the settings for a round stud lego brick
cmds.frameLayout(collapsable=True, label="Round Stud", width=475, height=140)

cmds.columnLayout()

#Size Settings
cmds.intSliderGrp('roundStudHeight',l="Height", f=True, min=1, max=20, value=1)

#Colour Settings
cmds.colorSliderGrp('roundStudColour', label="Colour", hsv=(120, 1, 1))

#modifier settings
cmds.checkBox('plainCylinder', l='Plain Cylinder', v=0)
cmds.columnLayout()

#create brick
cmds.button(label="Create Round Stud", command=('roundStud()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#create axle
cmds.frameLayout(collapsable=True, label="Axle", width=475, height=140)

cmds.columnLayout()

#Size Settings
cmds.intSliderGrp('axleLength',l="Length", f=True, min=1, max=5, value=4)

#Colour Settings
cmds.colorSliderGrp('axleColour', label="Colour", hsv=(120, 1, 1))
cmds.columnLayout()

#create brick
cmds.button(label="Create Axle", command=('axle()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

#Setting for adding transparacy to any brick
cmds.frameLayout(collapsable=True, label="General Settings", width=475, height=140)

#Make brick clear setting
cmds.checkBox ('makeClear', l='Make Clear', v=0)
cmds.columnLayout()
cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.showWindow( MyWin )


#Function for creating the basic brick
def basicBlock():
    
    #Gathering size settings
    blockHeight = cmds.intSliderGrp('blockHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('blockWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('blockDepth', q=True, v=True)
    
    #Gathering colour settings
    rgb = cmds.colorSliderGrp('blockColour', q=True, rgbValue=True)
    
    #Gathering modifer settings
    addSideStud = cmds.checkBox('addSideStud', query=True, v=True)
    makeClear = cmds.checkBox('makeClear', query=True, v=True)
    makeSideHole = cmds.checkBox('makeSideHole', query=True, v=True)
    makeMultSideHoles = cmds.checkBox('makeMultSideHoles', query=True, v=True)
    makeArch = cmds.checkBox('makeArch', query=True, v=True)
    makeTopStudsHollow = cmds.checkBox('makeTopStudsHollow', query=True, v=True)
    makeAxleHole = cmds.checkBox('makeAxleHole', query=True, v=True)
    
    #Give the brick a name and random number
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    #Changing brick size depending on the settings
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    #Create the base cube
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    #Add the brick studs
    count = 1
    for i in range(blockWidth):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
            
            # hollow out studs
            if makeTopStudsHollow is True:
                #get the top face of the stud
                stud = nsTmp + ":pCylinder" + str(count) + ".f[21]"
                count = count+1
                
                #extrude the face
                cmds.polyExtrudeFacet(stud, scale=(0.8, 0.8, 0.8))
                cmds.polyExtrudeFacet(stud, translateY=(-0.199))
    
    #Merge the pieces together
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    #Delete the shape history
    cmds.delete(ch=True)
    
    #If the make side hole modifer is checked, the height is greater than 2, and the mutually exclusive mods are false
    if makeSideHole is True and addSideStud is False and makeMultSideHoles is False and makeArch is False and makeAxleHole is False and blockHeight > 2:
        
        #Create a Cylinder that will push through the piece and place it correctly
        cmds.polyCylinder(r=0.25, h=cubeSizeX+0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeY - 0.375), moveY=True, a=True)
        
        #two more cylinders for the notches on the ends and place them correcly
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeX/2 + 0.01),(cubeSizeY - 0.375), moveX=True,  moveY=True, a=True)
        
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((-cubeSizeX/2 - 0.01),(cubeSizeY - 0.375), moveX=True,  moveY=True, a=True)
        
        #turn the three cylinders into on shape
        cmds.polyCBoolOp(nsTmp + ":pCylinder1", nsTmp + ":pCylinder2", nsTmp + ":pCylinder3", operation=1)
        
        #Delete the shape history
        cmds.delete(ch=True)
        
        #boolean remove the combined cylinders from the piece
        cmds.polyCBoolOp(nsTmp + ":" + nsTmp, nsTmp + ':polySurface1', operation=2)
        
        #Delete the shape history
        cmds.delete(ch=True)
    
    #If the make multiple side hole modifier is checked, the height is > 2, and the mutually exclusive mods are false
    if makeMultSideHoles is True and makeSideHole is False and makeArch is False and addSideStud is False and makeAxleHole is False and blockHeight > 2:
        
        #Create 2 cyliners that will push thru the piece and place them correctly
        cmds.polyCylinder(r=0.25, h=cubeSizeX+0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeY - 0.375), (cubeSizeZ/4), moveY=True, moveZ=True, a=True)
        
        cmds.polyCylinder(r=0.25, h=cubeSizeX+0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeY - 0.375), -(cubeSizeZ/4), moveY=True, moveZ=True, a=True)
        
        #four more cylinders for the indented ends, place them correctly
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeX/2 + 0.01),(cubeSizeY - 0.375), (cubeSizeZ/4), moveX=True,  moveY=True, moveZ=True, a=True)
        
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((-cubeSizeX/2 - 0.01),(cubeSizeY - 0.375), (cubeSizeZ/4), moveX=True,  moveY=True, moveZ=True, a=True)
        
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeX/2 + 0.01),(cubeSizeY - 0.375), -(cubeSizeZ/4), moveX=True,  moveY=True, moveZ=True, a=True)
        
        cmds.polyCylinder(r=0.3, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((-cubeSizeX/2 - 0.01),(cubeSizeY - 0.375), -(cubeSizeZ/4), moveX=True,  moveY=True, moveZ=True, a=True)
        
        #turn all cylinders into one shape
        cmds.polyCBoolOp(nsTmp + ":pCylinder1", nsTmp + ":pCylinder2", nsTmp + ":pCylinder3", nsTmp + ":pCylinder4", nsTmp + ":pCylinder5", nsTmp + ":pCylinder6", operation=1)
        
        #delete shape history
        cmds.delete(ch=True)
        
        #boolean remove the combined cylinders from the piece
        cmds.polyCBoolOp(nsTmp + ":" + nsTmp, nsTmp + ':polySurface1', operation=2)
        
        #delete shape history
        cmds.delete(ch=True)
    
    #If the add side stud modifer is checker, the height is greater than 2 and the make hole is false
    if addSideStud is True and makeSideHole is False and makeMultSideHoles is False and makeArch is False and makeAxleHole is False and blockHeight > 2:
        
        #Create a Cylinder that will become the stud and place it correctly
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeX/2 + 0.10), (cubeSizeY - 0.375), moveX=True,  moveY=True, a=True)
        
        #Select the top piece of the stud        
        print("Shape Info", nsTmp,":pCylinder1.f[6]")
        myShape = nsTmp + ":pCylinder1.f[21]"
        print(myShape)
        cmds.select(myShape)
                
        #extrude the faces to make the hollow stud
        cmds.polyExtrudeFacet(myShape, scale=(0.8, 0.8, 0.8))
        cmds.polyExtrudeFacet(myShape, translateX=(-0.199))
        
        #combine the shapes
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
        
        #Delete the shape history
        cmds.delete(ch=True)
    
    #If makeArch modifier is checked, the height is > 2, and the mutually exclusive mods are false
    if makeArch is True and addSideStud is False and makeSideHole is False and makeMultSideHoles is False and makeAxleHole is False and blockHeight > 2:
        
        #create a cylinder to push thru the piece
        cmds.polyCylinder(r=0.5, h=cubeSizeX+0.20)
        cmds.rotate(0, 0 , -90)
        cmds.move((cubeSizeY - 0.75), moveY=True, a=True)
        
        #create a cube to push thru the piece
        cmds.polyCube(w=cubeSizeX+0.2, h=0.5, d=1)
        cmds.move((cubeSizeY - 1), moveY=True, a=True)
        
        #combine cylinder and cube
        cmds.polyCBoolOp(nsTmp + ":pCylinder1", nsTmp + ":pCube1", operation=1)
        
        #delete shape history
        cmds.delete(ch=True)
        
        #boolean remove arch from the piece
        cmds.polyCBoolOp(nsTmp + ":" + nsTmp, nsTmp + ':polySurface1', operation=2)
        
        #delete shape history
        cmds.delete(ch=True)
    
    #if makeAxleHole is checked, the height is > 2, and the mutually exclusive mods are false
    if makeAxleHole is True and addSideStud is False and makeSideHole is False and makeMultSideHoles is False and makeArch is False and blockHeight > 2:
        
        #create an axle to push thru the piece
        cmds.polyCube(w=cubeSizeX+0.2, h=0.4, d=0.15)
        cmds.polyCube(w=cubeSizeX+0.2, h=0.4, d=0.15)
        cmds.rotate(90, 0, 0)
        
        #combine cubes
        cmds.polyCBoolOp(nsTmp + ":pCube1", nsTmp + ":pCube2", operation=1)
        
        #delete shape history
        cmds.delete(ch=True)
        
        #move axle into position
        cmds.move((cubeSizeY - 0.375), moveY=True, a=True)
        
        #remove axle from the block
        cmds.polyCBoolOp(nsTmp + ":" + nsTmp, nsTmp + ':polySurface1', operation=2)
        
        #delete shape history
        cmds.delete(ch=True)
    
    #rename the shape
    cmds.rename(nsTmp+":"+nsTmp, ignoreShape=True)
    
    #make the material
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    
    #if the clear modifer is checked
    if makeClear is True:
        #make the shape transparent
        cmds.setAttr(nsTmp+":blckMat.transparency",0.9,0.9,0.9, typ='double3')
        
    #select the whole shape and assign the new material
    cmds.select(nsTmp+":"+nsTmp)
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    #rename the shape
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)


#Function for creating the tile brick
def tileBlock():
    #Gathering size settings
    blockHeight = cmds.intSliderGrp('tileBlockHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('tileBlockWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('tileBlockDepth', q=True, v=True)
    
    #Gathering colour settings
    rgb = cmds.colorSliderGrp('tileBlockColour', q=True, rgbValue=True)
    
    #Gathering modifer settings
    addCentralStud = cmds.checkBox('addTileCentralStud', query=True, v=True)
    makeClear = cmds.checkBox('makeClear', query=True, v=True)
    
    #Give the brick a name and random number
    nsTmp = "tileBlock" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    #Changing brick size depending on the settings
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    #Create the base cube
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    #If add central stud is false
    if addCentralStud is False:
        #make the material
        myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
        myShape = nsTmp + ":pCube1"
        
        #if the clear modifer is checked
        if makeClear is True:
            #make the shape transparent
            cmds.setAttr(nsTmp+":blckMat.transparency",0.9,0.9,0.9, typ='double3')
            
        #make the material
        cmds.select(myShape)
        cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
        
        #Delete the shape history
        cmds.delete(ch=True)
        
        #Add the colour to the material
        cmds.hyperShade(assign=(nsTmp+":blckMat"))
        
        #rename the shape
        cmds.rename(nsTmp, ignoreShape=True)
        cmds.namespace(removeNamespace=":"+nsTmp, mergeNamespaceWithParent=True)
    
    #If add central stud is true
    elif addCentralStud is True:
        #create the cylinder for the stud and position it
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        
        #Grab the top face of the cylinder        
        myShape = nsTmp + ":pCylinder1.f[21]"
        cmds.select(myShape)
                
        #extrude the face
        cmds.polyExtrudeFacet(myShape, scale=(0.8, 0.8, 0.8))
        cmds.polyExtrudeFacet(myShape, translateY=(-0.199))
                
        #make the new material        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
        
        #if the clear modifer is checked
        if makeClear is True:
            #make the shape transparent
            cmds.setAttr(nsTmp+":blckMat.transparency",0.9,0.9,0.9, typ='double3')
            
        #Add the colour to the material
        cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
        
        #Combine the shapes and delete the shape history    
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
        cmds.delete(ch=True)
        
        #assign the material    
        cmds.hyperShade(assign=(nsTmp+":blckMat"))
        
        #rename the shape
        cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)


#Function for creating the round 1x1 stud    
def roundStud():
    #force the brick size to be 1x1
    blockWidth = 1
    blockDepth = 1
    
    #Gathering size settings
    blockHeight = cmds.intSliderGrp('roundStudHeight', q=True, v=True)
    
    #Gathering colour settings
    rgb = cmds.colorSliderGrp('roundStudColour', q=True, rgbValue=True)
    
    #Gathering modifer settings
    makeClear = cmds.checkBox('makeClear', query=True, v=True)
    plainCylinder = cmds.checkBox('plainCylinder', q=True, v=True)
    
    #Give the brick a name and random number
    nsTmp = "roundStud" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    #Changing brick size depending on the settings
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    #change generation depending on plainCylinder
    if plainCylinder is False:
        #create the top stud
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        
        #create the stud middle
        cmds.polyCylinder(r=0.375, h=0.10)
        cmds.move((cubeSizeY - 0.05), moveY=True)
        
        #create the stud base
        cmds.polyCylinder(r=0.30, h=0.3)
        cmds.move((cubeSizeY/2.0 - 0.02), moveY=True, a=True)
        
        #combine the shapes
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    else:
        #create just the one cylinder
        cmds.polyCylinder(r=cubeSizeX/2, h=cubeSizeY)
        cmds.move((cubeSizeY/2), moveY=True, a=True)
        
        #rename the shape
        cmds.rename(nsTmp, ignoreShape=True)
    
    #delete shape history
    cmds.delete(ch=True)
    
    #create a new material
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    
    #if the clear modifer is checked
    if makeClear is True:
        #make the shape transparent
        cmds.setAttr(nsTmp+":blckMat.transparency",0.9,0.9,0.9, typ='double3')
        
    #select the shape
    cmds.select(nsTmp + ':' + nsTmp)
    
    #colour the material and assign it to the shape
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    #rename the shape
    cmds.rename(nsTmp, ignoreShape=True)
    cmds.namespace(removeNamespace=":"+nsTmp, mergeNamespaceWithParent=True)


#function for creating the corner block
def cornerBlock():
    #force the brick size to be 2x2
    blockWidth = 2
    blockDepth = 2
    
    #Gathering size settings
    blockHeight = cmds.intSliderGrp('cornerBlockHeight', q=True, v=True)
    
    #Gathering colour settings
    rgb = cmds.colorSliderGrp('cornerBlockColour', q=True, rgbValue=True)
    
    #Gathering modifer settings
    makeClear = cmds.checkBox('makeClear', query=True, v=True)
    
    #Give the brick a name and random number
    nsTmp = "cornerBlock" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    #Changing brick size depending on the settings
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    #Create the base cube
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    #Add the studs for the shape
    for i in range(blockWidth):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
        
    #combine the shapes of the piece
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    
    #create a cube that will cut a portion of the piece
    cmds.polyCube(h=blockHeight * 0.8, w=0.8, d=0.8)
    
    #move it to the correct location of the cut
    cmds.move(0.4, (cubeSizeY/1.5), 0.4, moveX=True, moveY=True, moveZ=True)
    
    #using boolean remove the portion of the shape
    cmds.polyCBoolOp(nsTmp + ":" + nsTmp, nsTmp + ':pCube1', operation=2)
  
    #Delete the shape history
    cmds.delete(ch=True)
    
    #make a new material
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    
    #If the clear modifer is selected
    if makeClear is True:
        #Make the shape transparent
        cmds.setAttr(nsTmp+":blckMat.transparency",0.9,0.9,0.9, typ='double3')
    
    #select the shape
    cmds.select(nsTmp + ':polySurface1')
    
    #assign the material
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    #rename the piece
    cmds.rename(nsTmp, ignoreShape=True)
    cmds.namespace(removeNamespace=":"+nsTmp, mergeNamespaceWithParent=True)


#function for creating the axle piece
def axle():
    #get length
    axleLength = cmds.intSliderGrp('axleLength', q=True, v=True)
    
    #Gathering colour settings
    rgb = cmds.colorSliderGrp('axleColour', q=True, rgbValue=True)
    
    #Give the brick a name and random number
    nsTmp = "Axle" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    #change axle length depending on settings
    cubeLength = axleLength * 0.8
    
    #create the cubes and place them correctly
    cmds.polyCube(w=cubeLength, h=0.4, d=0.15)
    cmds.move(0.2, moveY=True)
    
    cmds.polyCube(w=cubeLength, h=0.4, d=0.15)
    cmds.rotate(90, 0, 0)
    cmds.move(0.2, moveY=True)
    
    #combine cubes
    cmds.polyCBoolOp(nsTmp + ":pCube1", nsTmp + ":pCube2", operation=1)
    
    #delete shape history
    cmds.delete(ch=True)
    
    #make a new material
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    
    #select the shape
    cmds.select(nsTmp + ':polySurface1')
    
    #assign the material
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    #rename the piece
    cmds.rename(nsTmp, ignoreShape=True)
    cmds.namespace(removeNamespace=":"+nsTmp, mergeNamespaceWithParent=True)