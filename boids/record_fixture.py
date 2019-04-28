import yaml

variables = {'N_boids': 50, 'speed': 0.01, 'coll_avoid': 100, 'speed_match': 0.125, 'closeness':10000}

with open("fixture.yml", 'w') as stream:
        stream.write(yaml.dump(variables))