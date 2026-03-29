from voronoi_simple import nearest_site, voronoi_grid, voronoi_boundaries, lloyd_relaxation
idx, d = nearest_site((0,0), [(1,0),(10,10)])
assert idx == 0
grid = voronoi_grid([(0,0),(10,10)], 20, 20, 5)
assert len(grid) == 4
assert grid[0][0] == 0  # closer to (0,0)
assert grid[3][3] == 1  # closer to (10,10) — (15,15) is closer to (10,10)
bounds = voronoi_boundaries([(0,0),(10,10)], 20, 20, 5)
assert len(bounds) > 0
relaxed = lloyd_relaxation([(0,0),(10,0)], 20, 20, 2)
assert len(relaxed) == 2
print("voronoi_simple tests passed")
