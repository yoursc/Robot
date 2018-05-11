
(cl:in-package :asdf)

(defsystem "pi_robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BMP180" :depends-on ("_package_BMP180"))
    (:file "_package_BMP180" :depends-on ("_package"))
    (:file "Distance" :depends-on ("_package_Distance"))
    (:file "_package_Distance" :depends-on ("_package"))
    (:file "Serial_Send" :depends-on ("_package_Serial_Send"))
    (:file "_package_Serial_Send" :depends-on ("_package"))
    (:file "Speed" :depends-on ("_package_Speed"))
    (:file "_package_Speed" :depends-on ("_package"))
  ))