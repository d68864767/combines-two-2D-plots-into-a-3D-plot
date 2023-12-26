```python
# Import necessary modules
from data_processing import interpolate_data, cluster_points
from plotting import create_3d_plot
from utils import load_data

def main():
    # Load data
    ranges, angles, power = load_data()

    # Interpolate data
    interpolated_data = interpolate_data(ranges, angles, power)

    # Cluster points
    clustered_data = cluster_points(interpolated_data)

    # Create 3D plot
    create_3d_plot(clustered_data)

if __name__ == "__main__":
    main()
```
