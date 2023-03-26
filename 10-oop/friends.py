class Friends:
    def __init__(self, connections: list | tuple):
        unique_pairs = []
        for pair in connections:
            if pair not in unique_pairs:
                unique_pairs.append(pair)
        self.__connections = unique_pairs

    def get_connections(self):
        return self.__connections

    def names(self):
        return set.union(*self.__connections)

    def add(self, connection: set):
        if connection not in self.__connections:
            self.__connections.append(connection)
            return True
        return False

    def remove(self, connection: set):
        if connection in self.__connections:
            self.__connections.remove(connection)
            return True
        return False

    # TODO: think about whether it could be done easier
    def connected(self, name: str):
        return set(
            element
            for pair in self.__connections
            for element in pair
            if name in pair
            if element != name
        )


# Check constructor
pair_one = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
print(pair_one.get_connections())
print(f"Connected functions: {pair_one.names()}\n")


# Check add function
pair_two = Friends([{"1", "2"}, {"3", "1"}])
print(pair_two.get_connections())
print(pair_two.add({"1", "3"}))
print(f"After function add with existence pair: {pair_two.get_connections()}\n")


# Check remove function
pair_three = Friends([{"1", "2"}, {"3", "1"}])
print(pair_two.get_connections())
print(pair_two.remove({"1", "3"}))
print(f"After function remove wit existence pair: {pair_two.get_connections()}")
print(pair_two.remove({"4", "5"}))


# Check connected function
pair_four = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
print("Check connected function:")
print(pair_four.connected("a"))
print(pair_four.connected("d"))
print(pair_four.remove({"c", "a"}))
print(pair_four.connected("c"))
