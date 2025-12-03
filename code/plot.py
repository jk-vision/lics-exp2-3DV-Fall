import matplotlib.pyplot as plt # for visualization
import plotly.graph_objects as go #for interactive visualization
import numpy as np # for matrix manipulation

# plot 2D figure
def plotfigure(imgs, title='Plot'):
  fig, axes = plt.subplots(nrows=1, ncols=len(imgs), figsize=(10, 5))
  fig.suptitle(title, fontsize=12, y=0.95)
  for i in range(len(imgs)):
    axes[i].imshow(imgs[i])
  plt.show()

# plot camera + point cloud in 3D
def plot_cameras_with_points(R_list, T_list, K, points3D=None, colors=None):
  fig = go.Figure()

  def make_frustum(R, t, K, scale=0.1):
        fx = K[0, 0]
        fy = K[1, 1]
        cx, cy = K[0, 2], K[1, 2]
        corners = np.array([
            [0, 0, 0],
            [-cx/fx, -cy/fy, 1], # left top
            [ cx/fx, -cy/fy, 1], # right top
            [ cx/fx,  cy/fy, 1], # bottom right
            [ -cx/fx,  cy/fy, 1], #bottom left
        ])
        corners *= scale
        return (R @ corners.T) + t # (3, 5)

  for i, (R, t) in enumerate(zip(R_list, T_list)):
    frustum = make_frustum(R, t, K)
    color = f"rgb({50+i*30%200},{100+i*50%255},{150+i*70%255})" #camera color

    # add camera frustum
    for j in range(1, 5):
      fig.add_trace(go.Scatter3d(
          x=[frustum[0,0], frustum[0,j]],
          y=[frustum[1,0], frustum[1,j]],
          z=[frustum[2,0], frustum[2,j]],
          mode='lines',
          line=dict(color=color)
      ))

    for j in range(1, 5):
      next_j = j+1 if j<4 else 1
      fig.add_trace(go.Scatter3d(
          x=[frustum[0,j], frustum[0,next_j]],
          y=[frustum[1,j], frustum[1,next_j]],
          z=[frustum[2,j], frustum[2,next_j]],
          mode='lines',
          line=dict(color=color)
      ))

    # add camera center
    fig.add_trace(go.Scatter3d(
            x=[frustum[0,0]], y=[frustum[1,0]], z=[frustum[2,0]],
            mode='markers+text',
            marker=dict(size=4, color=color),
            text=[f"Cam {i+1}"],
            textposition="top center"
        ))

  # add triangulated points if available
  if points3D is not None:
      fig.add_trace(go.Scatter3d(
          x=points3D[:,0], y=points3D[:,1], z=points3D[:,2],
          mode='markers',
          marker=dict(size=2.1, color=colors),
          name='3D Points'
      ))

  fig.update_layout(
        scene=dict(aspectmode='data'),
        title="Camera Frustums (+ Triangulated Points)",
        showlegend=False
    )
  fig.show()