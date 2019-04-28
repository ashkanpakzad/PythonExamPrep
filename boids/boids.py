from matplotlib import pyplot as plt
from matplotlib import animation
import random
from argparse import ArgumentParser

class Boids:
    def __init__(self, N_boids, speed, coll_avoid, speed_match, closeness):
        self.N = N_boids
        self.min_xvel = 0.0
        self.max_xvel = 10.0
        self.min_yvel = -20.0
        self.max_yvel = 20.0
        self.min_xpos = -450.0
        self.max_xpos = 50.0
        self.min_ypos = 300.0
        self.max_ypos = 600.0
        self.xpos = [random.uniform(self.min_xpos,self.max_xpos) for x in range(self.N)]
        self.ypos = [random.uniform(self.min_ypos,self.max_ypos) for x in range(self.N)]
        self.xvel = [random.uniform(self.min_xvel,self.max_xvel) for x in range(self.N)]
        self.yvel = [random.uniform(self.min_yvel,self.max_yvel) for x in range(self.N)]
        self.coll_avoid = coll_avoid
        self.speed_mid = speed
        self.speed_match = speed_match
        self.closeness = closeness

    def check_distance(self, m, n):
        return (self.xpos[n]-self.xpos[m])**2 + (self.ypos[n]-self.ypos[m])**2
    
    def fly_mid(self, m, n):
        self.xvel[m]=self.xvel[m]+(self.xpos[n]-self.xpos[m])*self.speed_mid/self.N
        self.yvel[m]=self.yvel[m]+(self.ypos[n]-self.ypos[m])*self.speed_mid/self.N

    def prevent_coll(self, m, n):
        if self.check_distance(m,n) < self.coll_avoid:
            self.xvel[m]=self.xvel[m]+(self.xpos[m]-self.xpos[n])
            self.yvel[m]=self.yvel[m]+(self.ypos[m]-self.ypos[n])
        
    def match_speed(self, m, n):
        if self.check_distance(m,n) < self.closeness:
            self.xvel[m]=self.xvel[m]+(self.xvel[n]-self.xvel[m])*self.speed_match/self.N
            self.yvel[m]=self.yvel[m]+(self.yvel[n]-self.yvel[m])*self.speed_match/self.N
    
    def update_boids(self):
        for i in range(self.N):
            for j in range(self.N):
                self.fly_mid(i,j)
                self.prevent_coll(i,j)
                self.match_speed(i,j)
            	# Update position according to velocities
            self.xpos[i]=self.xpos[i]+self.xvel[i]
            self.ypos[i]=self.ypos[i]+self.yvel[i]
    
    def animate(self, frame):
       self.update_boids()
       scatter.set_offsets(list(zip(obj.xpos,obj.ypos)))
   

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate boid simulations")
    parser.add_argument('N_boids', type=int)
    parser.add_argument('--speed','-s', nargs='?', default=0.01, type=float)
    parser.add_argument('--coll_avoid','-ca', nargs='?', default=100.0, type=float)
    parser.add_argument('--speed_match','-sm', nargs='?', default=0.125, type=float)
    parser.add_argument('--closeness','-cl', nargs='?', default=10000.0, type=float)
    parser.add_argument('--N_frames','-f', nargs='?', default=50, type=int)
    parser.add_argument('--xlim','-xax', nargs='+', default=[-500,1500], type=int)
    parser.add_argument('--ylim','-yax', nargs='+', default=[-500,1500], type=int)
    parser.add_argument('--filename','-fn', nargs='?', default='anim.mp4', type=str)

    args= parser.parse_args()
    
    obj = Boids(args.N_boids, args.speed, args.coll_avoid, args.speed_match, args.closeness)
    figure=plt.figure()
    axes=plt.axes(xlim=args.xlim, ylim=args.ylim)
    scatter=axes.scatter(obj.xpos,obj.ypos) # First frame
    
    anim = animation.FuncAnimation(figure, obj.animate,
                                   frames=args.N_frames, interval=50)
    
    anim.save(args.filename)
    
# Saves output as video.
# corrected zip to list offsets.
# Defined var for num. boids
# Defined var for velocity distributions
# Defined var for initial pos distributions
# removed unnessisary repeating for loops in update_boids
# changed long range(len(etc)) to function var.
# Converted boids to class
# Split up update boids into individual units