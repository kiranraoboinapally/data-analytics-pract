import sys
print(sys.version);
print("Hello, World!");


a,b=10,3;
if a>b:
    print("a is greater than b");
else:
    print("a is not greater than b");
print("type(a):", type(a));
print("type(b):", type(b));

x="Hai this is a String";
print("type(x):", type(x));

x=10.56;
print("type(x):", type(x));

a=10;
b="3";
print("type(a):",str(type(a))+" "+" and type(b):", str(type(b)));
a=str(a);
b=int(b);
print("After conversion: ");

print("type(a):", type(a), "and type(b):", type(b));
print(f"type(a): {type(a)} and type(b): {type(b)}");