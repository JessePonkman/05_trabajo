from repositorios import Repositorios

class ProductoService:
    def add_producto(self, prod=None):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        lastKey += 1
        Repositorios.productosList[lastKey] = prod.__dict__
        return lastKey

    def delete_producto(self, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError

    def update_producto(self, prod, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
            Repositorios.productosList[key] = prod.__dict__
        else:
            raise ValueError
            
    def get_productosList(self):
        pass
