import folium

def create_trace_map(lat, lon, label="Target"):
    print(f"[+] Generating map for {label} at {lat}, {lon}")
    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], tooltip=label, icon=folium.Icon(color="red")).add_to(m)
    m.save("output/trace_map.html")
    print("[+] Map saved as output/trace_map.html")
