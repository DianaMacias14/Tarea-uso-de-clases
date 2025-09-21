class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben de ser positiva")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print("El producto ya es existente")
                return

        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"El producto '{nombre}' se agrego correctamente")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print("La cantidad deve de cer positiva")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"La venta se realizo: {cantidad} unidad (s)'{nombre}'.")
                else:
                    print("No hay suficiente stock para realizar su venta")
                return
        print("El producto no se pudo localizar en el inventario")

    def mostrar_inventario(self):
        print(f"\n Inventario de: {self.nombre_tienda}:")
        if not self.productos:
            print("El inventario se encuentra vacio")
        else:
            for producto in self.productos:
                print(f"- {producto['nombre']}: ${producto['precio']} | STOCK: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            print("No hay productos en inventario")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f"\n Producto mas caro: {producto_caro['nombre']} (${producto_caro['precio']})")



def menu():
    print("da clik para ir a menu")
    nombre_tienda = input("Tienda de tennis") 
    tienda = InventarioTienda(nombre_tienda)

    while True:
        print("\n OPCIONES:")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto mas")
        print("5. Salir")

        opcion = input("Selecciona una opción  (1,2,3,4 o 5): ")

        if opcion == "1":
            nombre = input("Nombre de producto: ")
            try:
                precio = float(input("Precio de producto: "))
                cantidad = int(input("Cantidad disponible: "))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Usa numeros para precio y cantidad")

        elif opcion == "2":
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Usa números enteros")

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print("Nos vemos!!")
            break

        else:
            print("La opcion no es valida")

menu()
