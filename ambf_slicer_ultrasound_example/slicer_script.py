transform = slicer.mrmlScene.GetFirstNodeByName('TumorTransform')
ros = slicer.util.getModuleLogic('ROS2')
node = ros.GetDefaultRos2Node()
publisher = node.CreateAndAddPublisherNode('Pose', 'tumor_transform_topic')

def updateTransform():
  matrix = vtk.vtkMatrix4x4()
  transform.GetMatrixTransformToParent(matrix)
  publisher.Publish(matrix)

transform.AddObserver(vtk.vtkMRMLTransformNode.TransformModifiedEvent, updateTransform)