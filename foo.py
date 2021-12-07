# foo.py
import bpy
# clear meshes in the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

bpy.ops.mesh.primitive_cone_add(location=(-3, 0, 0))

output = '/home/rag/Desktop/render.png'
bpy.context.scene.render.filepath = output
bpy.ops.render.render(write_still=True)

# run with
  # blender --background --python foo.py
