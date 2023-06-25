# OOPs concepts

## **Abstract and Interface**

### Abstract class and methods

- An *abstract class* is a class that is declared `abstract`—it may or may not include abstract methods. Abstract classes cannot be instantiated, but they can be subclassed.
- An *abstract method* is a method that is declared without an implementation (without braces, and followed by a semicolon), like this:
    
    `abstract void moveTo(double deltaX, double deltaY);`
    
- If a class includes abstract methods, then the class itself *must* be declared `abstract`
- **An Abstract Class Example**
    
    In an object-oriented drawing application, you can draw circles, rectangles, lines, Bezier curves, and many other graphic objects. These objects all have certain states (for example: position, orientation, line color, fill color) and behaviors (for example: moveTo, rotate, resize, draw) in common. Some of these states and behaviors are the same for all graphic objects (for example: position, fill color, and moveTo). Others require different implementations (for example, resize or draw). All `GraphicObject`s must be able to draw or resize themselves; they just differ in how they do it. This is a perfect situation for an abstract superclass. You can take advantage of the similarities and declare all the graphic objects to inherit from the same abstract parent object (for example, `GraphicObject`) as shown in the following figure.
    
    ![Classes Rectangle, Line, Bezier, and Circle Inherit from GraphicObject](https://docs.oracle.com/javase/tutorial/figures/java/classes-graphicObject.gif)
    
    Classes Rectangle, Line, Bezier, and Circle Inherit from GraphicObject
    
    First, you declare an abstract class, `GraphicObject`, to provide member variables and methods that are wholly shared by all subclasses, such as the current position and the `moveTo` method. `GraphicObject` also declares abstract methods for methods, such as `draw` or `resize`, that need to be implemented by all subclasses but must be implemented in different ways. The `GraphicObject` class can look something like this:
    
    ```java
    abstract class GraphicObject {
        int x, y;
        ...
        void moveTo(int newX, int newY) {
            ...
        }
        abstract void draw();
        abstract void resize();
    }
    ```
    
    Each non abstract subclass of `GraphicObject`, such as `Circle` and `Rectangle`, must provide implementations for the `draw` and `resize` methods:
    
    ```java
    class Circle extends GraphicObject {
        void draw() {
            ...
        }
        void resize() {
            ...
        }
    }
    class Rectangle extends GraphicObject {
        void draw() {
            ...
        }
        void resize() {
            ...
        }
    }
    ```
    

### Interface

### **Abstract Classes Compared to Interfaces**

Abstract classes are similar to interfaces. You cannot instantiate them, and they may contain a mix of methods declared with or without an implementation. However, with abstract classes, you can declare **fields** that are not static and final, and define public, protected, and private concrete methods. With interfaces, all **fields** are automatically public, static, and final, and all methods that you declare or define (as default methods) are public. In addition, you can extend only one class, whether or not it is abstract, whereas you can implement any number of interfaces. Note that many software libraries use both abstract classes and interfaces; the `HashMap` class implements several interfaces and also extends the abstract class `AbstractMap`.

Which should you use, abstract classes or interfaces?

- Consider using abstract classes if any of these statements apply to your situation:
    - You want to share code among several closely related classes.
    - You expect that classes that extend your abstract class have many common methods or fields, or require access modifiers other than public (such as protected and private).
    - You want to declare non-static or non-final fields. This enables you to define methods that can access and modify the state of the object to which they belong.
- Consider using interfaces if any of these statements apply to your situation:
    - You expect that unrelated classes would implement your interface. For example, the interfaces `[Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)` and `[Cloneable](https://docs.oracle.com/javase/8/docs/api/java/lang/Cloneable.html)` are implemented by many unrelated classes.
    - You want to specify the behavior of a particular data type, but not concerned about who implements its behavior.
    - You want to take advantage of multiple inheritance of type.

### **When an Abstract Class Implements an Interface**

In the section on `[Interfaces](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html)`, it was noted that a class that implements an interface must implement *all* of the interface's methods. It is possible, however, to define a class that does not implement all of the interface's methods, provided that the class is declared to be `abstract`. For example,

```java
abstract class X implements Y {
  // implements all but one method of Y
}

class XX extends X {
  // implements the remaining method in Y
}
```

In this case, class `X` must be `abstract` because it does not fully implement `Y`, but class `XX` does, in fact, implement `Y`.

### **References**

1. [https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html)