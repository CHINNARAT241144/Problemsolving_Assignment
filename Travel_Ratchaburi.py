import folium
import sqlite3
import networkx as nx
import matplotlib.pyplot as plt

sqlfile = 'Data_PB_Assingment.db'
network = nx.Graph()

#ฟังก์ชั่นMenu แสดงหน้าตาเมนูของโปรแกรม
def menu():
    print("เมนู:")
    print("1. กดหนดจุดหมายการเที่ยว")
    print("2. เพิ่มข้อมูลการท่องเที่ยว")
    print("3. ลบข้อมูลในการท่องเที่ยว")
    print("4. แก้ไขข้อมูลการท่องเที่ยว")
    print("5. ออกจากโปรแกรม")




#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล Latitude จาก Database เพื่อนำมาใช้โปรแกรม
def get_node_Latitude():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT Latitude 
                                FROM NodeDetail;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        Latitude  = []
        for i in record:
            for n in i :
                Latitude.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (Latitude)
         

Latitude = get_node_Latitude()


#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล Longitude จาก Database เพื่อนำมาใช้โปรแกรม
def get_node_Longitude():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT Longitude 
                                FROM NodeDetail;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        Longtitude  = []
        for i in record:
            for n in i :
                Longtitude.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (Longtitude)
         

Longitude = get_node_Longitude()


#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล NameNode จาก Database เพื่อนำมาใช้โปรแกรม
def get_node_Name():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT NameNode 
                                FROM NodeDetail;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        NameNode  = []
        for i in record:
            for n in i :
                NameNode.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (NameNode)
         
NameNode = get_node_Name()


#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล ลิงค์ที่อยู่ของรูปภาพ จาก Database เพื่อนำมาใช้โปรแกรม
def get_Link():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT PictureLink 
                                FROM NodeDetail;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        P_link  = []
        for i in record:
            for n in i :
                P_link.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (P_link)
         
P_link = get_Link()



#ฟังก์ชั่นที่ทำหน้าที่ในการ นำข้อมูล Latitude,longitude,NameNode,PictureLink มาใช้ในการสร้าง Mark  บน Map เพื่อแสดงบนเว็บไซต์
def Map_pojp(Latti,Longi,Name,image):

    mapOjp = folium.Map(location=(13.471001255344845, 99.63278267103284), zoom_start= 9.5)

    for lat,long,img,name in zip(Latti,Longi,image,Name):

        folium.Marker([lat, long],
        tooltip='Click me!', 
        popup=folium.Popup(f"""
                    <img src="{img}" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>     
                    <h4>{name}<br/></h4>
                    """, max_width=500), 
        icon=folium.Icon(icon='glyphicon glyphicon-tree-deciduous', color='Bule')).add_to(mapOjp)
        
        
    mapOjp
    mapOjp.save("index.html")



network = nx.Graph()



#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล หมายเลข Node ต้นทาง(Source) จาก Database เพื่อนำมาใช้ในการคำนวนหาระยะทางที่สั้นที่สุดในโปรแกรม
def get_Source_n():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT Source 
                                FROM EdgeNode;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        source_n  = []
        for i in record:
            for n in i :
                source_n.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (source_n)
         

source_n = get_Source_n()


#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล หมายเลข Node ปลายทาง(Destination) จาก Database เพื่อนำมาใช้ในการคำนวนหาระยะทางที่สั้นที่สุดในโปรแกรม
def get_Destination_n():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT Destination 
                                FROM EdgeNode;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        des_n  = []
        for i in record:
            for n in i :
                des_n.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (des_n)
         

des_n = get_Destination_n()



#ฟังก์ชั่นที่ทำหน้าที่ในการ ดึงข้อมูล หมายเลข Node ปลายทาง(Destination) จาก Database เพื่อนำมาใช้ในการคำนวนหาระยะทางที่สั้นที่สุดในโปรแกรม
def get_Distance_n():

    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT Distance 
                                FROM EdgeNode;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        distance_n  = []
        for i in record:
            for n in i :
                distance_n.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (distance_n)
         
distance_n = get_Distance_n()





#ฟังก์ชั่นที่ทำหน้าที่ในการ ระยะทางที่สั้นที่สุด โดยการนำข้อมูล หมายเลขNodeต้นทา และปลายทาง  ระยะทาง มาใช้หาระยาทางที่สั้นที่สุด
def find_Distance (source_n,des_n,distance_n,Name):

    #แสดงรายการจุดท่องเที่ยว
    a = 1
    for n in Name:
        print(a,'. ',n)
        a = a+1

    All_node_total = []
    # print(len(distance_n))
    for x in range (1,(len(distance_n)+1)):
        All_node_total.append(x)
    # print(All_node_total)

    network.add_nodes_from(All_node_total)
    # print(f"This network has now {network.number_of_nodes()} nodes.")

    # ดึงขอมูลจาก Database มาทำการสร้าง Node
    for s,d,w in zip(source_n,des_n,distance_n):
        network.add_edge(s, d, weight = w) 
    
    #เพิ่มสีลงในNode
    color_list = []
    for x in range (1,(len(distance_n)+1)):
        col = "Red"
        All_node_total.append(col)

    plt.figure(figsize=(8, 6))
    plt.title('Example of Graph Representation', size=10)

    source = int(input("จุดเริ่มต้น(ใส่เป็นตัวเลข): "))
    target = int(input("จุดหมายที่ต้องการไป(ใส่เป็นตัวเลข): "))
    shortest_path = nx.shortest_path(network, source, target, weight='weight')

    total_weight_decimal_shortest_path = sum(network[shortest_path[i]][shortest_path[i+1]]['weight'] 
                                            for i in range(len(shortest_path)-1) 
                                                if isinstance(network[shortest_path[i]][shortest_path[i+1]]['weight'], float))

    format_total_weight = f"{total_weight_decimal_shortest_path:.1f}"
    print(f"ระยะทางทั้งหมด: {format_total_weight} km.")
    nx.draw_networkx(network,node_color=color_list, with_labels=True)

    list_name_Node = []
    name_path =[]

    for v in  shortest_path:
        value = 0
        value = v-1
        list_name_Node.append(value)
    
    for np in list_name_Node:
        name_path.append(NameNode[np])

    print('จุดท่องเที่ยวที่เดินทางผ่าน:  ',name_path)

    return (shortest_path)




#ฟังก์ชั่นที่ทำหน้าที่ในการ สร้างเส้นทาง ที่ ผ่านแต่ละจุด บน Map
def make_line (short_path,Latti,Longi,Name,image):
    print()
    mapOjp = folium.Map(location=(13.471001255344845, 99.63278267103284), zoom_start= 9.5)
    lat = 0.00
    long = 0.00
    new_short =[]
    start = []
    end = []
    count =len(short_path)
    r = 1
    e_r = 0

    for lat,long,img,name in zip(Latti,Longi,image,Name):

        folium.Marker([lat, long],
        tooltip='Click me!', 
        popup=folium.Popup(f"""
                    <img src="{img}" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>     
                    <h4>{name}<br/></h4>
                    """, max_width=500), 
        icon=folium.Icon(icon='glyphicon glyphicon-tree-deciduous', color='Bule')).add_to(mapOjp)
           


    for x in short_path:
        a = 0
        a = x-1
        # print(a)
        new_short.append(a)

    for round in new_short:
        # print(round)

        # print(Latitude[round],Longitude[round])
        lat = Latitude[round]
        long = Longitude[round]
        if r < count:
            start.append([Latitude[round],Longitude[round]])
            r=r+1
        if e_r >= 1:
            end.append([Latitude[round],Longitude[round]])
        e_r = e_r+1
    
    for i,j in zip(start,end):

        folium.PolyLine(locations=[i, j], color='blue').add_to(mapOjp)

    mapOjp
    mapOjp.save("index.html")



#ฟังก์ชั่นที่ทำหน้าที่ในการ เพิ่ม สถานที่ท่องเที่ยวใหม่ ลงไปในDatabase โดยรับค่า (หมายเลขID,latitude,longitude,NameNode,Linkที่อยู่รูปภาพ)
def insert_Node():
    def insert_New_marker(NodeID, Latitude, Longitude, NameNode, PictureLink):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO NodeDetail
                            (NodeID, Latitude, Longitude, NameNode, PictureLink) 
                            VALUES (?, ?, ?, ?, ?);"""

            data_tuple = (NodeID, Latitude, Longitude, NameNode, PictureLink)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("New Node inserted successfully \n")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite:", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    print('ปัจจุบัน NodID ล่าสุดคือ :',len(Latitude))
    Node_id = int(input('กำหนด(NodeID) เป็นหมายเลข เช่น 1 เป็นต้น: '))
    NameNode_n = input('กรอกชื่อสถานที่ใหม่ที่คุณต้องการเพิ่มเข้าไปในฐานข้อมูล: ')
    Latitude_n = float(input('ตำแหน่งละติจูด (สามารถ copy ได้จาก Google Map): '))
    Longitude_n = float(input('ตำแหน่งลองจิจูด (สามารถ copy ได้จาก Google Map): '))
    link_pic = input('ลิงค์เว็บ รูปภาพ: ')

    insert_New_marker(Node_id, Latitude_n, Longitude_n, NameNode_n, link_pic)



#ฟังก์ชั่นที่ทำหน้าที่ในการ เพิ่ม เส้นเชื่อม ระหว่างจุด ลงไปในDatabase โดยรับค่า (หมายเลขID,หมายเลขIDจุดเริ่มต้น,หมายเลขIDจุดปลายทาง,ค่าของระยะทางของเส้นเชื่อม)
def insert_EdgeNode():
    def insert_New_Edge(EdgeID, Source, Destination, Distance):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO EdgeNode
                            (EdgeID, Source, Destination, Distance) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (EdgeID, Source, Destination, Distance)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("New Node inserted successfully \n")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite:", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
    print('ปัจจุบัน EdgeID ล่าสุดคือ :',len(source_n))
    Edge_id = int(input('กำหนด(EdgeID) เป็นหมายเลข เช่น 1 เป็นต้น: '))
    Source_n = int(input('กรอกจุดเริ่มต้นของเส้นทาง (NodID) เช่น 1 เป็นต้น: '))
    Destination_n = int(input('กรอกจุดสิ้นเส้นทาง (NodID) เช่น 1 เป็นต้น: '))
    Distance_n = float(input('กรอกระยะทางของเส้นทางหน่วย Km. เช่น 20  เป็นต้น: '))


    insert_New_Edge(Edge_id, Source_n, Destination_n, Distance_n)



#ฟังก์ชั่นที่ทำหน้าที่ในการ ลบ ข้อมูลของสถานท่องเที่ยวนั้นทิ้ง โดยการระบุ  หมายเลขID ของNode
def Delete_Node():
    def del_node(NodeID):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_update_query = """DELETE from NodeDetail where NodeID = ?"""
            cursor.execute(sql_update_query, (NodeID,))
            sqliteConnection.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    print('ปัจจุบัน NodeID ล่าสุดคือ :',len(Latitude))
    delete_node = int(input('คุณต้องการลบ NodeID  ใด: '))
    del_node(delete_node)



#ฟังก์ชั่นที่ทำหน้าที่ในการ ลบ ข้อมูลของเส้นเชื่อม โดยการระบุ  หมายเลขID ของEdgeNode
def Delete_Egde():
    def del_EdgeID (EdgeID):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_update_query = """DELETE from EdgeNode where EdgeID = ?"""
            cursor.execute(sql_update_query, (EdgeID,))
            sqliteConnection.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    print('ปัจจุบัน EdgeID ล่าสุดคือ :',len(source_n))
    delete_edge = int(input('คุณต้องการลบ EdgeID  ใด: '))
    del_EdgeID(delete_edge)

#ฟังก์ชั่นสำหรับทำการ อัปเดตข้อมูล table EdgeNode โดยจะทการอัปเดตทั้งหมดทุก แอทริบิ้ว ยกเว้น EdgeID
def Update_NodeDetail():
    def update_NodeDetail (Id_Node,Lat_node,Long_node,Name_Node,link_img):
            try:
                sqliteConnection = sqlite3.connect(sqlfile)
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update NodeDetail set Latitude = ?, Longitude = ?, NameNode = ?, PictureLink = ? WHERE NodeID = ?"""
                
                data = (Lat_node,Long_node,Name_Node,link_img,Id_Node)
                cursor.execute(sql_update_query, data)
                sqliteConnection.commit()
                print("Record Updated successfully")
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to update sqlite table", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The sqlite connection is closed")

    print('ปัจจุบัน NodID ล่าสุดคือ :',len(Latitude))
    Id_Node = int(input('กรอกหมายเลขNodID ที่ต้องการแก้ไข ต้องการแก้ไขข้อมูลใด: '))
    Lat_node = input('longitudeใหม่: ')
    Long_node = input('latitudeใหม่: ')
    Name_Node = input('ชื่อของสถานที่ใหม่ที่ต้องการแก้ไข: ')
    link_img = input('ลิงค์รูปภาพใหม่: ')
    update_NodeDetail(Id_Node,Lat_node,Long_node,Name_Node,link_img)
   

#ฟังก์ชั่นสำหรับทำการ อัปเดตข้อมูล table NodeDetail โดยจะทการอัปเดตทั้งหมดทุก แอทริบิ้ว ยกเว้น NodeID
def Update_EdgeDetail():
    def update_EdgeDetail(Edge_ID, Source_N, Destination_N, Distance_N):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """UPDATE EdgeNode SET Source = ?, Destination = ?, Distance = ? WHERE EdgeID = ?"""

            data = (Source_N, Destination_N, float(Distance_N), Edge_ID)
            cursor.execute(sql_update_query, data)
            sqliteConnection.commit()
            print("Record Updated successfully")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The sqlite connection is closed")

    print('ปัจจุบัน EdgeID ล่าสุดคือ :',len(source_n))
    Edge_ID = int(input('ต้องการแก้ข้อมูล EdgeID ใด: '))
    Source_N = int(input('กรอกหมายเลขต้นทางใหม่ (จำเป็น): '))
    Destination_N = int(input('กรอกหมายเลขปลายทางใหม่ (จำเป็น): '))
    Distance_N = input('ระยะทางใหม่: ')
    update_EdgeDetail(Edge_ID, Source_N, Destination_N, Distance_N)




def main():
    Map_pojp(Latitude,Longitude,NameNode,P_link)
    while True:
        menu()
        choice = input("กรุณาเลือกหมายเลขที่ต้องการ: ")

        if choice == '1':
            print("กดหนดจุดหมายจุดเริ่มต้น-จุดปลายทาง")
            short_path = find_Distance(source_n,des_n,distance_n,NameNode)
            make_line (short_path,Latitude,Longitude,NameNode,P_link)

        elif choice == '2':
            print("1. เพิ่มสถานที่\n2. เพิ่มเส้นทางจุดเริ่ม ถึง ปลายทาง")
            sta = int(input("กรุณาใส่หมายเลขที่ต้องการทำรายการ: "))
            if sta == 1:
                insert_Node()
            elif sta == 2:
                insert_EdgeNode()
            else:
                print("กรุณาเลือกหมายเลขให้ถูกต้อง")

        elif choice == '3':
            print("1. ลบ สถานที่โดยใส่ NodeID เช่น 1 \n2. ลบ เส้นเชื่อมที่โดยใส่ EdgeID เช่น 12")
            Da = int(input("กรุณาใส่หมายเลขที่ต้องการทำรายการ: "))
            if Da == 1:
                Delete_Node()
            elif Da == 2:
                Delete_Egde()
            else:
                print("กรุณาเลือกหมายเลขให้ถูกต้อง")
        elif choice == '4':
            print("1. แก้ไข สถานที่โดยใส่ NodeID  \n2. แก้ไข สถานที่โดยใส่ EdgeID ")
            Pa = int(input("กรุณาใส่หมายเลขที่ต้องการทำรายการ: "))
            if Pa == 1:
                Update_NodeDetail()
            elif Pa == 2:
                Update_EdgeDetail()
            else:
                print("กรุณาเลือกหมายเลขให้ถูกต้อง")
  
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกหมายเลขให้ถูกต้อง")

if __name__ == "__main__":
    main()
