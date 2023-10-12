
 [UML Class Diagram Tutorial](https://www.youtube.com/watch?v=UI6lqHOVHic)

 [0:08](https://www.youtube.com/watch?v=UI6lqHOVHic&t=8)
![[Pasted image 20221013224452.jpg]]
UML Class Diagram

 [0:11](https://www.youtube.com/watch?v=UI6lqHOVHic&t=11)
![[Pasted image 20221013224503.jpg]]
- The basics of UML class diagrams
- Relationships in UML class diagrams
- How to interpret UML class diagrams

 [0:50](https://www.youtube.com/watch?v=UI6lqHOVHic&t=50)
 ![[Pasted image 20221013224509.jpg]]
The purpose of a class is to represent some entity in the system being modeled.

 [1:13](https://www.youtube.com/watch?v=UI6lqHOVHic&t=73)
 ![[Pasted image 20221013224514.jpg]]
Attributes are significant pieces of data that contain values that describe each instance of a class.

 [1:36](https://www.youtube.com/watch?v=UI6lqHOVHic&t=96)
 ![[Pasted image 20221013224551.jpg]]
Visibility is optional, but if you include it, it goes first. After that, you write the attribute's name in lowercase, followed by a colon and the data type.

 [1:52](https://www.youtube.com/watch?v=UI6lqHOVHic&t=112)
 ![[Pasted image 20221013224608.jpg]]
In Unified Modeling Language (UML), methods are the behavior-related parts of each class in an object-oriented program. These methods specify how objects in a program interact with each other and how they modify or retrieve data.

 [2:25](https://www.youtube.com/watch?v=UI6lqHOVHic&t=145)
 ![[Pasted image 20221013224613.jpg]]
Visibility refers to the ability of other classes to see or access a given property or class member.

 [3:05](https://www.youtube.com/watch?v=UI6lqHOVHic&t=185)
 ![[Pasted image 20221013224620.jpg]]
The symbols for visibility in UML are the minus sign, the plus sign, the hash, and the tilde.

The minus sign indicates that an attribute or method is private, the plus sign indicates that an attribute or method is public, the hash indicates that an attribute or method is protected, and the tilde indicates that an attribute or method has package or default visibility.

 [3:35](https://www.youtube.com/watch?v=UI6lqHOVHic&t=215)
 ![[Pasted image 20221013224627.jpg]]
Private attributes: name, employee ID, phone number, and department.
Public method: updating the phone number.

 [5:19](https://www.youtube.com/watch?v=UI6lqHOVHic&t=319)
 ![[Pasted image 20221013224634.jpg]]
Abstraction is a process of hiding the implementation details from the user and showing only functionality.

 [5:29](https://www.youtube.com/watch?v=UI6lqHOVHic&t=329)
 ![[Pasted image 20221013224640.jpg]]
Inheritance is when a child class inherits the attributes and methods of a parent class.

 [5:53](https://www.youtube.com/watch?v=UI6lqHOVHic&t=353)
 ![[Pasted image 20221013224648.jpg]]
An association relationship is a relationship between two classes in which one class is associated with the other.

 [6:23](https://www.youtube.com/watch?v=UI6lqHOVHic&t=383)
 ![[Pasted image 20221013224657.jpg]]
An aggregation relationship is a special type of association that specifies a whole and its parts. In other words, it is a relationship between a group of objects and the individual objects that make up the group.

 [7:04](https://www.youtube.com/watch?v=UI6lqHOVHic&t=424)
![[Pasted image 20221013224705.jpg]]
A composition relationship between two classes exists when the child class couldn't exist without the parent class. In other words, the child object is an integral part of the parent object.

 [7:32](https://www.youtube.com/watch?v=UI6lqHOVHic&t=452)
![[Pasted image 20221013224714.jpg]]
Multiplicity allows you to set numerical constraints on your relationships.

 [7:48](https://www.youtube.com/watch?v=UI6lqHOVHic&t=468)
![[Pasted image 20221013224718.jpg]]
Other types of multiplicity are zero to one, one to many, or a specific number range.

 [8:25](https://www.youtube.com/watch?v=UI6lqHOVHic&t=505)
![[Pasted image 20221013224730.jpg]]
The user class consists of attributes for user ID, password, login status, and register date; and a public method for verified login, returning a Boolean.

 [8:50](https://www.youtube.com/watch?v=UI6lqHOVHic&t=530)
 ![[Pasted image 20221013224734.jpg]]
The customer class is a class that inherits from the user class. It has its own specific attributes and methods, like being able to register, login and update the profile.

 [8:59](https://www.youtube.com/watch?v=UI6lqHOVHic&t=539)
 ![[Pasted image 20221013224738.jpg]]
Composition relationships are when the parts cannot exist without the whole. For example, if an instance of the customer class was destroyed, his shopping cart and orders would be lost. They can't exist outside of the customer.

 [9:27](https://www.youtube.com/watch?v=UI6lqHOVHic&t=567)
 ![[Pasted image 20221013224743.jpg]]
Multiplicity is used to indicate how many of one thing are related to another. In the first example, the multiplicity indicates that a customer can have zero or many orders. This means that a customer may never place an order, or they may place multiple orders. 

 [9:49](https://www.youtube.com/watch?v=UI6lqHOVHic&t=589)
 ![[Pasted image 20221013224748.jpg]]
In the second example, the multiplicity indicates that each order has one and only one order detail. This means that each order can only have one set of order details.


