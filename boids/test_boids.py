from boids import Boids
import pytest
import yaml

def import_vars():	
    with open("fixture.yml", 'r') as stream:
        data = yaml.load(stream)
    return data

# Test: invoking class with default variables returns reasonable boids.
def test_invoke():
    default_vars = import_vars()
    Boids(**default_vars) 

# Test: distance
def test_check_distance():
        default_vars =  import_vars()
        obj = Boids(**default_vars)
        obj.xpos[0] = 0.0
        obj.ypos[0] = 0.0
        obj.xpos[1] = 3.0
        obj.ypos[1] = 4.0
        assert obj.check_distance(0, 1) == 25.0

# Test: fly_mid
#def test_fly_mid():
#        default_vars = import_vars()
#        obj = Boids(**default_vars)
#        obj.xpos[0] = 0.0
#        obj.ypos[0] = 0.0
#        obj.xpos[1] = 3.0
#        obj.ypos[1] = 4.0
#        assert obj.check_distance(0, 1) == 25.0

# Test: prevent collision near
def test_prevent_coll_nochange():
        default_vars = import_vars()
        obj = Boids(**default_vars)
        obj.xpos[0] = 0.0
        obj.ypos[0] = 0.0
        obj.xpos[1] = 100
        obj.ypos[1] = 100
        obj.prevent_coll(0, 1)
        assert obj.xpos[0] == 0
        assert obj.ypos[0] == 0
        
def test_prevent_coll_change():
        default_vars = import_vars()
        obj = Boids(**default_vars)
        obj.xpos[0] = 0.0
        obj.ypos[0] = 0.0
        obj.xvel[0] = 10
        obj.yvel[0] = 10
        obj.xpos[1] = 2
        obj.ypos[1] = 2
        obj.prevent_coll(0, 1)
        assert obj.xvel[0] == 10+(0-2)
        assert obj.yvel[0] == 10+(0-2)


# Test: prevent collision far

# Test: match_speed near

# Test: match_speed far

# Test update_boids
