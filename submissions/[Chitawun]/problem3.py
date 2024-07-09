import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    # สร้าง dictionary เพื่อเก็บระยะทางที่สั้นที่สุดจากจุดเริ่มต้นถึงแต่ละจุด
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # สร้าง priority queue เพื่อเก็บจุดที่ต้องสำรวจต่อไป
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # ถ้าถึงจุดสิ้นสุดแล้ว ให้คืนค่าระยะทาง
        if current_vertex == end:
            return current_distance
        
        # ถ้าระยะทางปัจจุบันมากกว่าที่บันทึกไว้ ให้ข้ามไป
        if current_distance > distances[current_vertex]:
            continue
        
        # สำรวจเส้นทางที่เชื่อมต่อกับจุดปัจจุบัน
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # ถ้าพบเส้นทางที่สั้นกว่า ให้อัปเดตระยะทาง
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # ถ้าไม่พบเส้นทางไปยังจุดสิ้นสุด
    return float('infinity')

def create_graph(edges):
    graph = defaultdict(dict)
    for start, end, weight in edges:
        graph[start][end] = weight
        graph[end][start] = weight  # ถ้าเป็นกราฟแบบไม่มีทิศทาง
    return graph

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'D', 3),
        ('C', 'D', 1),
        ('C', 'E', 5),
        ('D', 'E', 2)
    ]

    graph = create_graph(edges)
    start = 'A'
    end = 'E'

    shortest_distance = dijkstra(graph, start, end)
    print(f"ระยะทางที่สั้นที่สุดจาก {start} ไป {end} คือ: {shortest_distance}")
