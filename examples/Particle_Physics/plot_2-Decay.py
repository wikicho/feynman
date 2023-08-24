# 2 body decay diagram 

import matplotlib.pyplot as plt
from feynman import Diagram

plt.rcParams["text.usetex"] = True

fig = plt.figure(figsize=(10.,10.))
ax = fig.add_axes([0,0,1,1], frameon=False)

diagram = Diagram(ax, draggable=True)
#i1 = diagram.vertex(xy=(.15, .6), marker="")
#i2 = diagram.vertex(xy=(.15, .2), marker="")
v1 = diagram.vertex(xy=(0.15, 0.5), marker="")
v2 = diagram.vertex(xy=(0.5, 0.5), marker="")
o1 = diagram.vertex(xy=(0.75, 0.8), marker="")
o2 = diagram.vertex(xy=(0.75, 0.2), marker="")

#f1 = diagram.line(i1, v1, arrow = True)
#f2 = diagram.line(i2, v1, arrow = True)
w1 = diagram.line(v1, v2, arrow=False)
f3 = diagram.line(o1, v2, arrow = True)
f4 = diagram.line(v2, o2, arrow = True)

opts = {"fontsize": 30}
#i1.text(r"$\bar{\nu}_e (p_1)$",    .003,  .035, **opts)
#i2.text(r"$e^- (p_2)$",           -.005, -.037, **opts)
o1.text(r"$\bar{i}_3$",  .006,  .035, **opts)
o2.text(r"$i_4$",          .024, -.032, **opts)
w1.text(r"$X$",              .340,  .054, **opts)

diagram.plot()
plt.savefig("./results/Decay.pdf")
#plt.show()

# If text element have been dragged, then their relative coordinates are
# updated accordingly. Let us print those.
for drawable in (o1, o2, w1):
    s, x, y, _ = drawable.texts[0]
    print("{:24s} {:6.3f} {:6.3f}".format(s, x, y))
