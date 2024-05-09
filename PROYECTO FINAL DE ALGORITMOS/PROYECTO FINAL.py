import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import networkx as nx
import random

# Función para cerrar la ventana de Tkinter
def on_closing():
    root.quit()
    root.destroy()

# Función para dibujar el camino más corto en la figura de Matplotlib
def dibujar_camino_mas_corto(G, complete_tour, ax):
    shortest_path = []
    for i in range(len(complete_tour) - 1):
        start_node = complete_tour[i]
        end_node = complete_tour[i + 1]
        shortest_path.extend(nx.shortest_path(G, source=start_node, target=end_node, weight='weight'))
        shortest_path.pop()  # Eliminar el último nodo para evitar duplicados

    # Dibujar la línea verde a lo largo del camino más corto
    for i in range(len(shortest_path) - 1):
        start_node = shortest_path[i]
        end_node = shortest_path[i + 1]
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
        edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos=nx.get_node_attributes(G, 'pos'), edgelist=edges, edge_color='green', width=2, ax=ax)

    # Actualizar la figura
    fig.canvas.draw()

# Función para encontrar el camino más corto entre dos nodos
def dijkstra_shortest_path(G, source, target):
        shortest_path = nx.dijkstra_path(G, source=source, target=target)
        return shortest_path

# Función para encontrar el camino más corto entre todos los nodos
def tsp_shortest_path(G):
        root = tk.Tk()
        root.title("Recorrido Completo")
        root.geometry("400x800")
        root.resizable(False, False)

        frame = ttk.Frame(root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        listbox.pack(fill="both", expand=True)

        scrollbar.config(command=listbox.yview)

        school_node = 300
        house_nodes = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215]

        # Encontrar todos los caminos más cortos entre todos los nodos
        all_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

        all_nodes = [school_node] + house_nodes

        complete_tour = [school_node]

        current_node = school_node

        edges_taken = []

        while len(complete_tour) < len(all_nodes):
            min_distance = float('inf')
            next_node = None

# Encontrar el nodo más cercano que no ha sido visitado
            for node in all_nodes:
                if node not in complete_tour:
                    distance = all_shortest_paths[current_node][node]
                    if distance < min_distance:
                        min_distance = distance
                        next_node = node

            edges_taken.append((current_node, next_node))

            complete_tour.append(next_node)

            current_node = next_node
    
        edges_taken.append((complete_tour[-1], school_node))
        complete_tour.append(school_node)
        total_distance = sum(all_shortest_paths[complete_tour[i]][complete_tour[i + 1]] for i in range(len(complete_tour) - 1))
        # Encontrar las intersecciones en el recorrido completo
        crossroads = [(node, pos) for node, pos in G.nodes(data='pos') if node in complete_tour]


        movements = []
        # Encontrar los movimientos de intersección a intersección
        for i in range(len(complete_tour) - 1):
            start_node = complete_tour[i]
            end_node = complete_tour[i + 1]
            path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
            for j in range(len(path) - 1):
                movements.append((path[j], path[j + 1]))

        # Mostrar los movimientos en la lista
        for movement in movements:
            start, end = movement
            listbox.insert("end", f"De intersección {start} a intersección {end}")
            
            
        dibujar_camino_mas_corto(G, complete_tour, ax)
        return complete_tour, total_distance, crossroads, edges_taken 

# Función para crear la ventana principal de Tkinter
def ventana_principal():

    global root, img, fig, ax, G
# Crear ventana de Tkinter
    root = tk.Tk()
    root.title("Visualización de Grafo")
    root.protocol("WM_DELETE_WINDOW", on_closing)
# Cargar la imagen de base
    img = plt.imread("mapa_gdl.png")

# Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(img)

# Crear un grafo dirigido
    G = nx.DiGraph()

# Agregar nodos con coordenanadas
    crossroads = [(1,  (847, 535)),
 (2,  (669, 606)),
 (3,  (616, 626)),
 (4,  (563, 646)),
 (5,  (501, 695)),
 (6,  (482, 721)),
 (7,  (455, 736)),
 (8,  (627, 516)),
 (9,  (613, 491)),
 (10,  (599, 463)),
 (11,  (664, 476)),
 (12,  (717, 469)),
 (13,  (693, 412)),
 (14,  (667, 365)),
 (15,  (626, 385)),
 (16,  (572, 414)),
 (17,  (551, 424)),
 (18,  (548, 371)),
 (19,  (539, 351)),
 (20,  (592, 321)),
 (21,  (583, 437)),
 (22,  (613, 312)),
 (23,  (627, 300)),
 (24,  (542, 253)),
 (25,  (473, 206)),
 (26,  (496, 275)),
 (27,  (478, 245)),
 (28,  (451, 190)),
 (29,  (406, 253)),
 (30,  (427, 270)),
 (31,  (458, 336)),
 (32,  (475, 365)),
 (33,  (497, 402)),
 (34,  (472, 419)),
 (35,  (530, 464)),
 (36,  (560, 517)),
 (37,  (551, 524)),
 (38,  (594, 552)),
 (39,  (582, 571)),
 (40,  (671, 492)),
 (41,  (514, 307)),
 (42,  (412, 162)),
 (43,  (433, 129)),
 (44,  (408, 96)),
 (45,  (443, 106)),
 (46,  (377, 134)),
 (47,  (343, 112)),
 (48,  (360, 91)),
 (49,  (373, 103)),
 (50,  (333, 63)),
 (51,  (319, 46)),
 (52,  (325, 73)),
 (53,  (338, 82)),
 (54,  (312, 94)),
 (55,  (290, 77)),
 (56,  (267, 151)),
 (57,  (258, 145)),
 (58,  (299, 173)),
 (59,  (331, 198)),
 (60,  (277, 205)),
 (61,  (245, 179)),
 (62,  (338, 255)),
 (63,  (262, 230)),
 (64,  (245, 218)),
 (65,  (252, 245)),
 (66,  (358, 329)),
 (67,  (235, 270)),
 (68,  (204, 245)),
 (69,  (181, 347)),
 (70,  (141, 309)),
 (71,  (173, 355)),
 (72,  (199, 383)),
 (73,  (159, 368)),
 (74,  (125, 334)),
 (75,  (115, 415)),
 (76,  (67, 368)),
 (77,  (91, 451)),
 (78,  (62, 459)),
 (79,  (44, 470)),
 (80,  (31, 399)),
 (81,  (27, 475)),
 (82,  (3, 409)),
 (83,  (11, 408)),
 (84,  (86, 523)),
 (85,  (65, 554)),
 (86,  (28, 564)),
 (87,  (1, 550)),
 (88,  (140, 444)),
 (89,  (184, 486)),
 (90,  (213, 519)),
 (91,  (269, 397)),
 (92,  (309, 375)),
 (93,  (326, 380)),
 (94,  (373, 396)),
 (95,  (380, 353)),
 (96,  (261, 459)),
 (97,  (243, 482)),
 (98,  (231, 425)),
 (99,  (212, 454)),
 (100,  (221, 517)),
 (101,  (422, 395)),
 (102,  (443, 439)),
 (103,  (456, 468)),
 (104,  (473, 451)),
 (105,  (420, 473)),
 (106,  (309, 483)),
 (107,  (292, 535)),
 (108,  (287, 572)),
 (109,  (210, 553)),
 (110,  (181, 547)),
 (111,  (208, 589)),
 (112,  (230, 593)),
 (113,  (227, 613)),
 (114,  (280, 606)),
 (115,  (276, 641)),
 (116,  (307, 652)),
 (117,  (327, 655)),
 (118,  (333, 620)),
 (119,  (342, 587)),
 (120,  (357, 675)),
 (121,  (299, 416)),
 (122,  (364, 451)),
 (123,  (356, 496)),
 (124,  (359, 515)),
 (125,  (389, 530)),
 (126,  (404, 505)),
 (127,  (483, 505)),
 (128,  (432, 553)),
 (129,  (470, 586)),
 (130,  (513, 552)),
 (131,  (541, 598)),
 (132,  (368, 565)),
 (133,  (349, 604)),
 (134,  (405, 586)),
 (135,  (497, 627)),
 (136,  (518, 656)),
 (137,  (469, 646)),
 (138,  (383, 625)),
 (139,  (388, 690)),
 (140,  (413, 643)),
 (141,  (443, 604)),
 (142,  (452, 593)),
 (143,  (319, 690)),
 (144,  (319, 735)),
 (145,  (475, 656)),
 (146,  (449, 672)),
 (147,  (431, 682)),
 (148,  (422, 709)),
 (149,  (415, 722)),
 (150,  (559, 634)),
 (151,  (504, 164)),
 (152,  (525, 128)),
 (153,  (506, 119)),
 (154,  (501, 127)),
 (155,  (541, 135)),
 (156,  (592, 177)),
 (157,  (603, 175)),
 (158,  (631, 201)),
 (159,  (667, 182)),
 (160,  (510, 73)),
 (161,  (480, 67)),
 (162,  (715, 300)),
 (163,  (739, 320)),
 (164,  (746, 342)),
 (165,  (706, 294)),
 (166,  (696, 252)),
 (167,  (706, 249)),
 (168,  (852, 209)),
 (169,  (816, 156)),
 (170,  (776, 129)),
 (171,  (751, 107)),
 (172,  (661, 59)),
 (173,  (692, 1)),
 (174,  (758, 85)),
 (175,  (794, 102)),
 (176,  (806, 82)),
 (177,  (781, 66)),
 (178,  (836, 99)),
 (179,  (851, 14)),
 (180,  (787, 12)),
 (181,  (816, 119)),
 (182,  (827, 142)),
 (183,  (408, 66)),
 (184,  (396, 58)),
 (185,  (410, 53)),
 (186,  (384, 32)),
 (187,  (397, 29)),
 (188,  (654, 632)),
 (189,  (669, 661)),
 (190,  (632, 677)),
 (191,  (672, 735)), ]
    for node, pos in crossroads:
        G.add_node(node, pos=pos)
 
# Agregar nodos de casas con coordenadas
    houses = [(200,  (313,  294)),
          (201,  (429,  221)),
          (202,  (645,  437)),
          (203,  (569,  280)),
          (204,  (322,  142)),
          (205,  (307,  230)),
          (206,  (91,  391)),
          (207,  (209,  307)),
          (208,  (253,  525)),
          (209,  (88,  490)),
          (210,  (443,  306)),
          (211,  (706,  442)),
          (212,  (402,  665)),
          (213,  (504,  482)),
          (214,  (308,  613)),
          (215,  (209,  571)),
            ]
    for node, pos in houses:
        G.add_node(node, pos=pos)
# Agregar nodo de escuela con coordenadas
    school = [(300,  (380,  293))]
    for node, pos in school:
        G.add_node(node, pos=pos)

# Agregar aristas 
    for u, v in [(1, 2),(2, 1),(2, 3),(3, 2),(3, 4),(4, 3),(4, 5),(5, 4),(5, 6),(6, 5),
            (6, 7),(7, 6),(2, 8),(8, 2),(8, 9),(9, 8),(9, 10),(10, 9),(10, 21),(21, 10),
            (21, 16),(16, 21),(16, 18),(18, 16),(18, 19),(19, 18),(19, 41),(41, 19),(41, 26),(26, 41),
            (26, 27),(27, 26),(27, 28),(28, 27),(28, 42),(42, 28),(42, 43),(43, 42),(43, 44),(44, 43),
            (43, 45),(45, 43),(45, 183),(183, 45),(183, 184),(184, 186),(186, 187),(187, 185),(185, 183),(42, 46),
            (46, 42),(46, 47),(47, 46),(47, 54),(54, 47),(54, 55),(55, 54),(8, 40),(40, 11),(11, 40),
            (40, 12),(12, 211),(211, 13),(13, 14),(14, 22),(22, 23),(23, 22),(13, 202),(202, 10),(16, 17),
            (17, 16),(16, 15),(15, 14),(14, 162),(162, 14),(162, 163),(163, 162),(163, 164),(164, 163),(28, 25),
            (25, 24),(24, 203),(203, 20),(20, 15),(22, 20),(20, 19),(26, 24),(51, 50),(50, 51),(48, 50),
            (50, 48),(56, 54),(54, 52),(52, 50),(52, 53),(53, 52),(48, 47),(48, 49),(49, 48),(47, 204),
            (204, 58),(58, 60),(60, 61),(61, 60),(60, 205),(205, 60),(205, 62),(62, 205),(60, 63),(63, 64)
            ,(64, 63),(63, 65),(65, 67),(67, 68),(68, 67),(67, 207),(207, 69),(69, 70),(70, 69),(69, 71),
            (71, 73),(73, 74),(74, 73),(73, 75),(75, 77),(77, 75),(75, 206 ),(77, 78),(78, 77),(78, 80),
            (80, 78),(78, 79),(79, 78),(79, 81),(81, 82),(82, 83),(83, 79),(77, 209),(209, 77),(209, 84),
            (84, 209),(84, 85),(85, 84),(85, 86),(86, 85),(86, 87),(87, 86),(57, 56),(56, 57),(56, 58),
            (58, 56),(58, 59),(59, 46),(59, 29),(28, 201),(201, 29),(29, 300),(29, 30),(300, 66),(30, 27),
            (30, 210),(210, 31),(41, 31),(31, 32),(32, 33),(33, 18),(33, 34),(34, 33),(33, 35),(21, 35),
            (35, 213),(213, 127),(35, 36),(36, 9),(37, 36),(130, 37),(129, 130),(3, 39),(39, 37),(37, 38),
            (38, 37),(39, 131),(131, 135),(135, 137),(131, 150),(150, 131),(135, 136),(136, 135),(65, 200),(200, 65),
            (200, 66),(66, 200),(66, 95),(95, 66),(95, 101),(101, 95),(101, 102),(102, 101),(102, 103),(103, 102),
            (103, 127),(127, 103),(127, 130),(130, 127),(130, 131),(131, 130),(101, 32),(103, 104),(104, 103),(135, 129),
            (129, 128),(128, 125),(125, 124),(127, 128),(128, 134),(134, 138),(138, 120),(132, 134),(134, 141),(141, 142),
            (142, 141),(141, 137),(137, 145),(145, 5),(145, 146),(146, 147),(147, 148),(148, 149),(6, 147),(148, 7),
            (95, 94),(94, 95),(94, 122),(122, 94),(122, 123),(123, 122),(123, 124),(124, 123),(124, 119),(119, 124),
            (119, 118),(118, 119),(118, 117),(117, 118),(117, 143),(143, 117),(143, 144),(144, 143),(102, 105),(105, 126),
            (126, 125),(125, 132),(132, 133),(133, 138),(138, 140),(140, 212),(212, 139),(139, 120),(120, 117),(117, 116),
            (116, 115),(115, 114),(114, 108),(108, 107),(107, 106),(114, 214),(214, 118),(119, 108),(103, 126),(122, 105),
            (91, 121),(121, 122),(66, 93),(94, 93),(93, 92),(92, 91),(91, 98),(98, 99),(99, 89),(75, 88),(88, 89),
            (89, 90),(108, 109),(109, 110),(110, 109),(109, 215),(215, 111),(111, 112),(112, 113),(113, 112),(112, 114),
            (90, 109),(90, 100),(100, 90),(107, 208),(208, 100),(121, 96),(96, 121),(96, 97),(97, 96),(97, 100),
            (100, 97),(97, 99),(123, 106),(106, 96),(96, 98),(98, 72),(72, 71),(88, 72),(72, 88),(162, 165),
            (165, 166),(166, 165),(166, 167),(167, 166),(165, 156),(156, 157),(157, 156),(156, 151),(151, 156),(25, 151),
            (151, 25),(151, 152),(152, 151),(152, 155),(155, 152),(152, 153),(153, 152),(153, 154),(154, 153),(157, 160),
            (160, 157),(160, 161),(161, 160),(157, 158),(158, 157),(158, 159),(159, 158),(159, 168),(168, 159),(168, 169),
            (169, 168),(169, 170),(170, 169),(170, 171),(171, 170),(171, 172),(172, 171),(172, 173),(173, 172),(170, 175),
            (175, 181),(181, 182),(182, 169),(175, 176),(176, 175),(176, 177),(177, 176),(176, 178),(178, 176),(176, 179),
            (179, 176),(174, 175),(171, 174),(174, 180),(180, 174),(2, 188),(188, 189),(189, 190),(190, 191),(191, 190),
            (190, 3), (206, 76), (76, 206), (206, 75)





            


             
         
             

]:
        weight = random.randint(1, 50)  # Generar un peso aleatorio entre 1 y 50
        G.add_edge(u, v, weight=weight)

# Obtener posiciones de los nodos
    node_pos = nx.get_node_attributes(G, 'pos')

# Obtener pesos de las aristas
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

# Dibujar el grafo
    nx.draw(G, node_pos, with_labels=True, node_size=30, node_color='skyblue', font_size=7, arrows=True)

#Dibujar nodos de casas con otro color
    nx.draw_networkx_nodes(G, node_pos, nodelist=[node[0] for node in houses], node_color='red', node_size=30)

#Dibujar nodo de escuela con otro color
    nx.draw_networkx_nodes(G, node_pos, nodelist=[node[0] for node in school], node_color='green', node_size=30)

#mostrar pesos de las aristas
    nx.draw_networkx_edge_labels(G, node_pos, edge_labels=edge_labels, font_color='black', font_size=5) 

# Crear lienzo para mostrar la figura de Matplotlib en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

# Colocar lienzo en la ventana de Tkinter
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear barra de herramientas de navegación (zoom)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear un marco para los botones y centrarlo en la ventana
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=10)

# Crear botones
    button1 = tk.Button(button_frame, text="Encontrar camino más corto", command=lambda: tsp_shortest_path(G))
    button1.pack(side=tk.LEFT, padx=5)

    button2 = tk.Button(button_frame, text="Salir", command=root.quit)
    button2.pack(side=tk.LEFT, padx=5)

# Ejecutar el bucle principal de Tkinter
    root.mainloop()

ventana_principal()