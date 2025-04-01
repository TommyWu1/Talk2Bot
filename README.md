# 🤖 Robot Commander Simulator  
**Control a virtual robot through a web interface!**  

Hey there! This is **Talk2Bot**, a project I built during my freetime to showcase my skills in programming. It lets you control a robot on a grid using text commands, complete with obstacles, battery life, and even a secret Easter egg. Think of it like a mini-game where you’re programming a robot’s movements—but with natural language!  

---

## 🕹️ Features  
- **Grid-based movement**: Move the robot around a 6x6 grid with obstacles  
- **Battery system**: Every move drains battery (turns yellow at 60%, red at 30%)  
- **Secret Easter egg**: Find the hidden "❓" tile for a surprise animation 🎉  
- **Error handling**: Red text alerts for invalid commands  
- **Web UI**: Simple interface with retro-cyberpunk vibes  

---

## 🚀 How to Run  
1. **Install requirements**:  
   ```bash  
   pip install flask
2. **Run the app**: using command python app.py in terminal
3. **Use it:** Open http://localhost:5000 in your browser
4. **Commands:** go to x,y (e.g., go to 1,5). Try reaching (5,5) for the secret celebration!

##🔧 Tech Stack
- **Backend:** Python + Flask (for handling commands)
- **Frontend:** Vanilla JavaScript + CSS animations
- **Pathfinding:** A* algorithm (with Manhattan distance)
- **Style:** Custom CSS with neon effects
   
##💡 Future Improvements
-Add voice commands using the browser’s speech API
-Let users place their own obstacles
