import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class PauseAnimation:
    def __init__(self,graph:list,time=4):
        self.graph = graph
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Click to pause/resume the animation')

        self.ax.set_ylim([self.graph.max(),self.graph.min()])
        self.p, = self.ax.plot(self.graph[0])
        
        self.animation = animation.FuncAnimation(
            self.fig, self.update, frames=len(self.graph), interval=len(self.graph)/time, blit=True)
        self.paused = True

        self.fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        self.p.set_ydata(self.graph[i])
        return (self.p,)