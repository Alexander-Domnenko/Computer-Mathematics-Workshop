from maclaurin import *


figure = plt.figure()
ax1 = figure.add_subplot(2, 3, 1)
ax2 = figure.add_subplot(2, 3, 2)
ax3 = figure.add_subplot(2, 3, 3)
ax4 = figure.add_subplot(2, 3, 4)
ax5 = figure.add_subplot(2, 3, 5)
ax1.set_title('e**x')
ax2.set_title('cos(x)')
ax3.set_title('sin(x)')
ax4.set_title('arcsin(x)')
ax5.set_title('arccos(x)')
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax5.grid(True)
ax1.plot(search_points(calculation_exp, 10, 5)[
        0], search_points(calculation_exp, 10, 5)[1])
ax2.plot(search_points(calculation_cos, 10, 5)[
         0], search_points(calculation_cos, 10, 5)[1])
ax3.plot(search_points(calculation_sin, 10, 1)[
         0], search_points(calculation_sin, 10, 1)[1])
ax4.plot(search_points(calculation_arcsin, 2, 3)[
         0], search_points(calculation_arcsin, 2, 3)[1])
ax5.plot(search_points(calculation_arccos, 2, 2)[
         0], search_points(calculation_arccos, 2, 2)[1])

plt.show()
