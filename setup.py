#Setup for Slither.py
import cx_Freeze 

executables = [
        cx_Freeze.Executable("slither.py") 
] 
cx_Freeze.setup( 
        name = "Slither",
        version = "1.0",
        options = {"build_exe": {"packages":["pygame"],"include_files":["Apple.png","SnakeHead.png","gameLogo.png"]}},
        description = "Slither game", 
        executables = executables)
