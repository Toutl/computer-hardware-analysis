import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Matplotlib
plt.style.use("/home/toutl/code/.machine.mplstyle")

wr_cmap = LinearSegmentedColormap.from_list("wr", ["#F2FFFC", "#FF6D7E"])
wg_cmap = LinearSegmentedColormap.from_list("wg", ["#F2FFFC", "#A2E57B"])
wp_cmap = LinearSegmentedColormap.from_list("wp", ["#F2FFFC", "#BAA0F8"])

dr_cmap = LinearSegmentedColormap.from_list("dr", ["#273136", "#FF6D7E"])
dg_cmap = LinearSegmentedColormap.from_list("dg", ["#273136", "#A2E57B"])
dp_cmap = LinearSegmentedColormap.from_list("dp", ["#273136", "#BAA0F8"])

rwg_cmap = LinearSegmentedColormap.from_list("rwg", ["#FF6D7E", "#F2FFFC", "#A2E57B"])
rdg_cmap = LinearSegmentedColormap.from_list("rwg", ["#FF6D7E", "#273136", "#A2E57B"])

complete_cmap = LinearSegmentedColormap.from_list(
    "complete", ["#FF6D7E", "#FFB270", "#FFED72", "#A2E57B", "#7CD5F1", "#BAA0F8"]
)
