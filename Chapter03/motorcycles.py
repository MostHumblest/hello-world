motorcycles=["honda", "yamaha", "suzuki"]
print (motorcycles)
motorcycles.append("ducati")
print(motorcycles)
motorcycles = []
print (motorcycles)
motorcycles.append("honda")
motorcycles.append("suzuki")
motorcycles.append("ducati")
print(motorcycles)
motorcycles.insert(0, "yamaha")
print(motorcycles)
del motorcycles[2]
print(motorcycles)
pop_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(pop_motorcycles)
motorcycles.append(pop_motorcycles)
print(motorcycles)

too_expensive="ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title() +" is too expensive for me.")

