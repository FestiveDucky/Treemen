import pygame, time, math
from random import randint as ri
from random import choice as ch

block_border_points0 = [(702, 140), (702, 140), (709, 137), (715, 135), (720, 132), (726, 129), (737, 124), (741, 123), (749, 119), (760, 116), (765, 114), (775, 112), (788, 109), (798, 108), (804, 107), (812, 107), (823, 107), (838, 108), (848, 109), (862, 112), (878, 117), (891, 121), (903, 124), (915, 125), (925, 127), (932, 129), (945, 135), (955, 139), (964, 142), (976, 146), (990, 150), (998, 153), (1005, 157), (1013, 160), (1027, 167), (1038, 171), (1045, 174), (1051, 177), (1058, 180), (1066, 184), (1074, 189), (1082, 193), (1095, 199), (1105, 203), (1117, 209), (1129, 214), (1144, 221), (1160, 232), (1175, 243), (1183, 249), (1194, 256), (1206, 264), (1216, 268), (1226, 273), (1234, 276), (1244, 281), (1254, 287), (1267, 293), (1276, 296), (1282, 299), (1287, 301), (1300, 305), (1320, 311), (1336, 316), (1349, 319), (1357, 321), (1372, 323), (1384, 325), (1397, 328), (1408, 331), (1418, 331), (1428, 331), (1441, 328), (1451, 325), (1461, 320), (1469, 316), (1478, 309), (1485, 304), (1493, 297), (1501, 291), (1511, 285), (1517, 279), (1521, 275), (1528, 267), (1539, 257), (1552, 245), (1560, 238), (1567, 230), (1581, 217), (1591, 205), (1606, 190), (1619, 177), (1629, 167), (1639, 159), (1654, 143), (1661, 136), (1672, 124), (1676, 121), (1682, 115), (1696, 104), (1705, 97), (1709, 93), (1711, 92), (1714, 90), (1715, 89), (1715, 89), (1719, 88), (1724, 88), (1736, 91), (1742, 95), (1745, 99), (1748, 105), (1751, 111), (1754, 120), (1759, 131), (1763, 140), (1766, 153), (1771, 166), (1776, 176), (1780, 186), (1783, 199), (1786, 205), (1789, 215), (1791, 221), (1792, 233), (1795, 246), (1798, 255), (1800, 272), (1802, 292), (1804, 303), (1805, 315), (1807, 326), (1809, 339), (1811, 356), (1811, 367), (1813, 380), (1813, 393), (1813, 401), (1810, 413), (1809, 418), (1805, 429), (1800, 450), (1799, 455), (1791, 467), (1776, 492), (1774, 496), (1769, 500), (1755, 514), (1746, 523), (1733, 533), (1712, 547), (1705, 551), (1685, 563), (1659, 581), (1656, 584), (1643, 589), (1625, 597), (1611, 602), (1604, 605), (1598, 608), (1579, 617), (1564, 627), (1553, 631), (1527, 645), (1513, 654), (1503, 659), (1490, 667), (1486, 671), (1470, 683), (1439, 711), (1434, 717), (1431, 720), (1428, 726), (1427, 733), (1424, 741), (1419, 753), (1414, 761), (1406, 772), (1398, 784), (1392, 792), (1387, 805), (1383, 817), (1377, 834), (1368, 852), (1360, 865), (1352, 878), (1349, 886), (1345, 896), (1335, 913), (1328, 923), (1318, 936), (1296, 970), (1290, 976), (1274, 978), (1266, 978), (1274, 971), (1267, 972), (1263, 973), (1259, 972), (1251, 969), (1244, 965), (1233, 957), (1220, 946), (1204, 937), (1188, 928), (1173, 917), (1160, 908), (1147, 899), (1141, 891), (1135, 883), (1128, 873), (1121, 863), (1112, 851), (1100, 838), (1090, 828), (1079, 815), (1070, 804), (1062, 795), (1051, 783), (1043, 772), (1031, 755), (1025, 748), (1019, 738), (1008, 725), (996, 712), (983, 696), (969, 679), (962, 672), (946, 656), (942, 650), (936, 641), (932, 636), (924, 624), (917, 612), (910, 597), (903, 585), (893, 570), (889, 567), (876, 558), (875, 557), (868, 550), (862, 539), (855, 525), (850, 514), (842, 496), (833, 474), (830, 470), (824, 464), (808, 446), (805, 441), (798, 431), (789, 417), (780, 405), (770, 390), (762, 378), (754, 365), (746, 350), (738, 335), (734, 325), (727, 311), (716, 287), (710, 275), (706, 265), (695, 232), (691, 219), (686, 208), (682, 192), (681, 182), (681, 147), (683, 125), (686, 124), (697, 124), (699, 123), (703, 123)]
block_border_points = [(664, 86), (664, 86), (664, 86), (666, 85), (671, 82), (679, 78), (687, 74), (697, 70), (707, 66), (724, 60), (734, 58), (744, 55), (752, 54), (761, 53), (772, 52), (783, 51), (792, 50), (803, 49), (811, 49), (819, 49), (825, 49), (834, 49), (844, 49), (854, 49), (869, 53), (888, 57), (905, 62), (915, 65), (926, 69), (936, 73), (948, 77), (964, 81), (979, 84), (991, 88), (996, 90), (1008, 95), (1026, 102), (1040, 108), (1056, 116), (1064, 120), (1067, 121), (1072, 124), (1076, 127), (1082, 131), (1093, 136), (1104, 142), (1122, 151), (1128, 154), (1145, 163), (1156, 168), (1171, 176), (1189, 184), (1225, 197), (1252, 204), (1257, 206), (1260, 207), (1268, 211), (1275, 216), (1284, 222), (1293, 229), (1307, 238), (1321, 248), (1330, 254), (1341, 260), (1351, 263), (1372, 267), (1387, 268), (1405, 268), (1422, 268), (1438, 266), (1448, 263), (1464, 255), (1475, 245), (1480, 238), (1490, 219), (1499, 205), (1507, 195), (1518, 182), (1527, 171), (1538, 159), (1550, 147), (1562, 135), (1570, 128), (1578, 119), (1600, 100), (1605, 96), (1615, 89), (1624, 83), (1630, 78), (1636, 74), (1644, 67), (1652, 62), (1662, 58), (1676, 53), (1694, 47), (1709, 43), (1717, 43), (1733, 43), (1750, 49), (1766, 55), (1771, 58), (1777, 66), (1787, 79), (1796, 91), (1804, 104), (1808, 114), (1812, 127), (1816, 135), (1817, 144), (1819, 153), (1820, 160), (1824, 173), (1827, 186), (1829, 194), (1832, 206), (1839, 233), (1841, 248), (1846, 269), (1848, 280), (1853, 302), (1856, 316), (1859, 328), (1860, 339), (1861, 346), (1863, 358), (1865, 369), (1865, 381), (1865, 397), (1865, 405), (1862, 416), (1856, 429), (1852, 440), (1846, 458), (1844, 466), (1841, 479), (1837, 495), (1833, 507), (1829, 518), (1821, 530), (1812, 542), (1799, 555), (1784, 566), (1779, 570), (1774, 574), (1766, 581), (1754, 591), (1743, 599), (1732, 606), (1720, 612), (1710, 617), (1696, 623), (1684, 628), (1678, 633), (1668, 639), (1649, 650), (1636, 656), (1626, 660), (1614, 663), (1606, 665), (1598, 667), (1593, 670), (1586, 672), (1581, 675), (1576, 677), (1573, 679), (1562, 687), (1553, 693), (1537, 705), (1529, 710), (1518, 715), (1512, 721), (1507, 724), (1501, 729), (1490, 738), (1483, 745), (1479, 750), (1473, 758), (1464, 777), (1460, 785), (1455, 800), (1449, 814), (1445, 824), (1438, 836), (1433, 844), (1426, 856), (1421, 870), (1416, 880), (1410, 891), (1405, 902), (1400, 911), (1394, 922), (1385, 936), (1379, 947), (1375, 954), (1367, 973), (1349, 1016), (1345, 1023), (1340, 1027), (1340, 1027), (1340, 1027), (1338, 1027), (1331, 1027), (1326, 1027), (1324, 1027), (1315, 1027), (1299, 1026), (1281, 1024), (1264, 1020), (1253, 1017), (1242, 1013), (1230, 1009), (1213, 1003), (1199, 999), (1184, 991), (1159, 977), (1142, 966), (1128, 954), (1116, 941), (1105, 931), (1085, 915), (1073, 904), (1062, 891), (1053, 876), (1043, 860), (1035, 846), (1027, 835), (1007, 815), (995, 804), (989, 797), (976, 782), (958, 760), (941, 740), (929, 725), (915, 706), (902, 689), (896, 680), (888, 668), (883, 661), (879, 656), (868, 641), (857, 622), (846, 606), (835, 590), (824, 575), (810, 556), (800, 544), (792, 532), (782, 519), (772, 505), (759, 488), (746, 471), (744, 468), (743, 465), (740, 459), (736, 450), (728, 436), (718, 415), (716, 410), (710, 391), (705, 375), (702, 367), (694, 344), (687, 325), (683, 317), (678, 307), (665, 274), (662, 265), (658, 256), (647, 223), (634, 167), (633, 163), (633, 163), (633, 152), (634, 146), (639, 128), (641, 118), (644, 106), (653, 82), (657, 69), (659, 67), (669, 63), (679, 58), (690, 54), (696, 52), (701, 52), (708, 52)]


class Cell(pygame.sprite.Sprite):
    def __init__(self, side_length, coords):
        super().__init__()
        self.side_length = side_length
        self.coords = coords
        self.point = None
        self.image = pygame.Surface((self.side_length - 1, self.side_length - 1))
        self.image.fill((30, 30, 30))
        self.rect = self.image.get_rect(x=self.coords[1] * self.side_length, y=self.coords[0] * self.side_length)

    def add_point(self, point):
        self.point = point


class Sampling:
    def __init__(self, x1, y1, x2, y2, candidate_samples, inner_circle_radius, outer_circle_radius,
                 thickness, circle_size):
        # x1, y1, x2, y2 are the dimensions on where to run the algorithm
        self.inner_circle_radius = inner_circle_radius
        self.outer_circle_radius = outer_circle_radius
        self.thickness = thickness
        self.circle_size = circle_size
        self.points = []
        self.available_points = []

        self.x1 = x1
        self.y1 = y1

        self.cell_side_length = int(self.inner_circle_radius / math.sqrt(2))
        # Making the dimensions evenly divisble by the cell side length
        self.x2 = x2 // self.cell_side_length * self.cell_side_length
        self.y2 = y2 // self.cell_side_length * self.cell_side_length
        self.x1 = x1 // self.cell_side_length * self.cell_side_length
        self.y1 = y1 // self.cell_side_length * self.cell_side_length

        self.cells = {}
        self.available_cells = {}
        for y in range(self.y1 // self.cell_side_length, self.y2 // self.cell_side_length):
            for x in range(self.x1 // self.cell_side_length, self.x2 // self.cell_side_length):
                new_cell = Cell(self.cell_side_length, (y, x))
                self.cells[(y, x)] = new_cell
                self.available_cells[(y, x)] = new_cell

        self.createPoints(candidate_samples)

    def draw(self, specific_point, gamedisplay, color, all=False):
        if all:
            # Draws the cells underneath the points for debugging
            # for cell in self.cells:
            #     self.gamedisplay.blit(self.cells[cell].image, self.cells[cell].rect)

            for point in self.points:
                pygame.draw.circle(gamedisplay, color, (point[1], point[0]), self.circle_size,
                                   self.thickness)

        else:
            pygame.draw.circle(gamedisplay, color, (specific_point[1], specific_point[0]),
                               self.circle_size, self.thickness)
        pygame.display.update()

    def checkEvents(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()

    def getPoints(self):
        return self.points

    def distance(self, other_point, current_point):
        vector = (current_point[0] - other_point[0], current_point[1] - other_point[1])
        dis = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        return dis

    def new_point(self, angle, distance, current_point):
        angle = math.radians(angle)
        return current_point[0] + (distance * math.sin(angle)), current_point[1] + (distance * math.cos(angle))

    def createPoints(self, candidate_samples):
        # Starting point
        current_point = ((self.y2 - self.y1) // 2 + self.y1, (self.x2 - self.x1) // 2 + self.x1)
        self.cells[
            (int(current_point[0] / self.cell_side_length), int(current_point[1] / self.cell_side_length))].add_point(
            current_point)
        self.points.append(current_point)
        self.available_cells.pop(
            (int(current_point[0] / self.cell_side_length), int(current_point[1] / self.cell_side_length)))
        self.available_points.append(current_point)

        while True:
            finished = False
            for i in range(candidate_samples):
                self.checkEvents()

                angle = ri(1, 360)
                distance = ri(self.inner_circle_radius, self.outer_circle_radius)
                new_candidate = self.new_point(angle, distance, current_point)
                if self.distance(tuple(map(round, new_candidate)), current_point) > self.outer_circle_radius:
                    new_candidate = tuple(map(int, new_candidate))
                else:
                    new_candidate = tuple(map(round, new_candidate))
                if self.y2 <= new_candidate[0] or new_candidate[0] < self.y1 or self.x2 <= new_candidate[1] or \
                        new_candidate[1] < self.x1:
                    continue

                point_cell = (
                int(new_candidate[0] / self.cell_side_length), int(new_candidate[1] / self.cell_side_length))

                if self.cells[point_cell].point is not None:
                    continue

                nearby_points = []
                for ny in range(point_cell[0] - 3, point_cell[0] + 3):
                    for nx in range(point_cell[1] - 3, point_cell[1] + 3):
                        if self.y1 // self.cell_side_length <= ny < self.y2 // self.cell_side_length and self.x1 // self.cell_side_length <= nx < self.x2 // self.cell_side_length and (
                        ny, nx) not in self.available_cells:
                            nearby_points.append(self.cells[(ny, nx)].point)

                distances = list(set(list(map(self.distance, nearby_points, [new_candidate] * len(nearby_points)))))
                failed = False
                for dis in distances:
                    if dis <= self.inner_circle_radius:
                        failed = True
                        break

                if failed:
                    continue

                percentage = 0.05
                skip_by = int(len(block_border_points) * percentage)
                list_to_check = block_border_points[:]
                while True:
                    closest = []
                    final = False
                    if skip_by <= 1:
                        final = True
                        skip_by = 1

                    for coords in list_to_check[0::skip_by]:
                        dis = self.distance((coords[1], coords[0]), new_candidate)
                        if len(closest) == 0:
                            closest = [coords, dis]
                        else:
                            if dis < closest[1]:
                                closest = [coords, dis]

                    if final:
                        if closest[1] < 80:
                            failed = True
                        break

                    index = list_to_check.index(closest[0])
                    if index < skip_by:
                        first = index
                        second = skip_by + 1
                    elif index >= len(block_border_points) - skip_by:
                        first = skip_by
                        second = (len(block_border_points) - index) + 1
                    else:
                        first = skip_by
                        second = skip_by + 1
                    list_to_check = list_to_check[index - first:index + second][:]
                    percentage += 0.1
                    skip_by = int(len(list_to_check) * percentage)

                if not failed:
                    self.points.append(new_candidate)
                    self.available_points.append(new_candidate)
                    self.cells[point_cell].add_point(new_candidate)
                    self.available_cells.pop(point_cell)
                    finished = True
                    break

            if not finished:
                self.available_points.remove(current_point)

            if len(self.available_points) > 0:
                current_point = ch(self.available_points)
            else:
                break
