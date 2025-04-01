from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

robot_position = (0, 0)
goal = (5, 5)
grid_size = 6
obstacles = {(2, 2), (3, 3), (4, 4)}
battery_level = 100

class AStarPathfinder:
    def __init__(self, grid_size, obstacles):
        self.grid_size = grid_size
        self.obstacles = obstacles

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self, start, goal):
        from queue import PriorityQueue
        open_set = PriorityQueue()
        open_set.put((0, start))
        came_from = {}
        g_score = {start: 0}

        while not open_set.empty():
            current = open_set.get()[1]
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if (0 <= neighbor[0] < self.grid_size and 
                    0 <= neighbor[1] < self.grid_size and 
                    neighbor not in self.obstacles):
                    tentative_g = g_score[current] + 1
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self.heuristic(neighbor, goal)
                        open_set.put((f_score, neighbor))
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    global robot_position, battery_level
    data = request.json
    command = data['command'].lower()
    
    if "go to" in command:
        parts = command.split(" ")
        x = int(parts[2].split(",")[0])
        y = int(parts[2].split(",")[1])
        goal = (x, y)
        pathfinder = AStarPathfinder(grid_size, obstacles)
        path = pathfinder.find_path(robot_position, goal)
        
        if path:
            battery_level -= len(path)
            robot_position = path[-1]
            return jsonify({
                "status": "success",
                "position": robot_position,
                "path": path,
                "battery": battery_level
            })
    
    return jsonify({"status": "error", "message": "Command not understood"})

if __name__ == '__main__':
    app.run(debug=True)