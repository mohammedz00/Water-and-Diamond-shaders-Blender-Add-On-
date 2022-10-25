#Import bpy
import bpy


#Info that can be added from object add on template
bl_info = 
{
    "name": "Shader Library",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D",
    "description": "Adds a new Shader to Object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Shader"
}

#Creating main panel


class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Special Shader"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = 'Diamond Shader')
        row.operator('shader.diamond_operator')
        
        row = layout.row()
        row.label(text = 'Water')
        row.operator('shader.water_operator')
        



#Creating custom operator for diamond shader

class Shader_OT_Diamond(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'
    
    def execute(self,context):
        
        #Creating new shader and calling it diamond
        material_diamond = bpy.data.materials.new(name = 'Diamond')
        #Enabling use nodes
        material_diamond.use_nodes = True
        #Removing the principled bsdf node
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        #Creating a reference to the Material Output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        #Set location of node
        material_output.location = (350, 225)
        


#       Adding glass1 node

        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
#       Setting location of node
        glass1_node.location = (-600, 650)
        #Setting the default color, the tuple shows R,G,B,Alpha
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        #Setting the default IOR value
        glass1_node.inputs[2].default_value = 1.446
        
        
        
#       Adding glass2 node
        
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #Setting location of node
        glass2_node.location = (-600, 450)
        #Setting the default color, the tuple shows R,G,B,Alpha
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        #Setting the default IOR value
        glass2_node.inputs[2].default_value = 1.450
        
        
        
    #   Adding glass3 node
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #Setting location of node
        glass3_node.location = (-600, 250)
        #Setting the default color, the tuple shows R,G,B,Alpha
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        #Setting the default IOR value
        glass3_node.inputs[2].default_value = 1.450
        
        
        
    #   Adding glass4 node
        
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #Setting location of node
        glass4_node.location = (-600, 50)
        #Setting the default color, the tuple shows R,G,B,Alpha
        glass4_node.inputs[0].default_value = (0, 0, 0, 1)
        #Setting the default IOR value
        glass4_node.inputs[2].default_value = 1.450
        
        
        
        
        
        
#       AddShader1
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        #Setting location of node
        add1_node.location = (-300, 425)
        #Setting a Label
        add1_node.label = 'Add 1'
        #Node is deslected by default
        add1_node.select = False
        
        
        
        
        #AddShader2
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        #Setting location of node
        add2_node.location = (-100, 250)
        #Setting a Label
        add2_node.label = 'Add 2'
        #Node is deselected by default
        add2_node.select = False
        
        
        
        # MixShader1
                
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        #Setting location of node
        mix1_node.location = (200, 220)
        #Setting a Label
        mix1_node.label = 'Mix 1'
        #Node is deselected by default
        mix1_node.select = False
        
        
        
#       Connecting inputs and outputs for the nodes
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        
        bpy.context.object.active_material = material_diamond
        
        
class Shader_OT_Water(bpy.types.Operator):
    bl_label = "Water"
    bl_idname = 'shader.water_operator'
    
    def execute(self,context):
        
        #Creating new shader and calling it diamond
        material_water = bpy.data.materials.new(name = 'Water')
        #Enabling use nodes
        material_water.use_nodes = True
        material_water.node_tree.nodes.remove(material_water.node_tree.nodes.get('Principled BSDF'))
        #Creating a reference to the Material Output
        material_output = material_water.node_tree.nodes.get('Material Output')
        #Set location of node
        material_output.location = (500, 500)
        
        # Adding Musgrave node

        musgrave_node = material_water.node_tree.nodes.new('ShaderNodeTexMusgrave')
#       Setting location of node
        musgrave_node.location = (-600, 650)
        #Setting the default color, the tuple shows R,G,B,Alpha
        musgrave_node.inputs[1].default_value = 0.500
        #Setting the default IOR value
        musgrave_node.inputs[2].default_value = 15.900
        musgrave_node.select = False
        
   
   
        # Adding Noise node

        noise_node = material_water.node_tree.nodes.new('ShaderNodeTexNoise')
#       Setting location of node
        noise_node.location = (-600, 350)
        #Setting the default color, the tuple shows R,G,B,Alpha
        noise_node.inputs[1].default_value = 4.900
        noise_node.select = False


        # Adding Mix node
        
        mix_node = material_water.node_tree.nodes.new('ShaderNodeMixRGB')
#       Setting location of node
        mix_node.location = (-300, 450)
        mix_node.select = False
        
        
        # Adding Bump node
        
        bump_node = material_water.node_tree.nodes.new('ShaderNodeBump')
#       Setting location of node
        bump_node.location = (-100, 450)
        bump_node.select = False
        
        # Adding pRINCIPLED node
        
        principled_node = material_water.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
#       Setting location of node
        principled_node.inputs[4].default_value = 1.000
        principled_node.inputs[7].default_value = 0.000
        principled_node.location = (100, 650)
        principled_node.select = False
        
        material_water.node_tree.links.new(musgrave_node.outputs[0], mix_node.inputs[1])
        material_water.node_tree.links.new(noise_node.outputs[0], mix_node.inputs[2])
        material_water.node_tree.links.new(mix_node.outputs[0], bump_node.inputs[2])
        material_water.node_tree.links.new(bump_node.outputs[0], principled_node.inputs[20])
        material_water.node_tree.links.new(principled_node.outputs[0], material_output.inputs[0])
        
        bpy.context.object.active_material = material_water




        
        return {'FINISHED'}
        
        
        
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(Shader_OT_Diamond)
    bpy.utils.register_class(Shader_OT_Water)
    


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(Shader_OT_Diamond)
    bpy.utils.unregister_class(Shader_OT_Water)


if __name__ == "__main__":
    register()

