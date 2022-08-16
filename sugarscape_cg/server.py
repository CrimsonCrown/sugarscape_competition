import mesa

from .agents import SsAgent, SsAgent2, Sugar
from .model import SugarscapeCg
from mesa.visualization.UserParam import UserSettableParameter

color_dic = {4: "#005C00", 3: "#008300", 2: "#00AA00", 1: "#00F800"}


def SsAgent_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is SsAgent:
        portrayal["Shape"] = "sugarscape_cg/resources/ant.png"
        portrayal["scale"] = 1.0
        portrayal["Layer"] = 1

    elif type(agent) is SsAgent2:
        portrayal["Shape"] = "sugarscape_cg/resources/redant.png"
        portrayal["scale"] = 0.8
        portrayal["Layer"] = 2

    elif type(agent) is Sugar:
        if agent.amount != 0:
            portrayal["Color"] = color_dic[agent.amount]
        else:
            portrayal["Color"] = "#D6F5D6"
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

model_params = {
    "width": 50,
    "height": 50,
    "initial_population": UserSettableParameter("slider", "Initial Population", 100, 0, 200, 1),
    "initial_population2": UserSettableParameter("slider", "Red Ant Population", 50, 0, 200, 1),
}


canvas_element = mesa.visualization.CanvasGrid(SsAgent_portrayal, 50, 50, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [{"Label": "SsAgent", "Color": "#AA0000"},{"Label": "SsAgentMassAvg", "Color": "#00AA00"}]
)

server = mesa.visualization.ModularServer(
    SugarscapeCg, [canvas_element, chart_element], "Sugarscape 2 Constant Growback", model_params
)
# server.launch()
