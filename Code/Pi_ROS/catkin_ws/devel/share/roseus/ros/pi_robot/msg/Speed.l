;; Auto-generated. Do not edit!


(when (boundp 'pi_robot::Speed)
  (if (not (find-package "PI_ROBOT"))
    (make-package "PI_ROBOT"))
  (shadow 'Speed (find-package "PI_ROBOT")))
(unless (find-package "PI_ROBOT::SPEED")
  (make-package "PI_ROBOT::SPEED"))

(in-package "ROS")
;;//! \htmlinclude Speed.msg.html


(defclass pi_robot::Speed
  :super ros::object
  :slots (_left _right ))

(defmethod pi_robot::Speed
  (:init
   (&key
    ((:left __left) 0)
    ((:right __right) 0)
    )
   (send-super :init)
   (setq _left (round __left))
   (setq _right (round __right))
   self)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:serialization-length
   ()
   (+
    ;; int16 _left
    2
    ;; int16 _right
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _left
       (write-word _left s)
     ;; int16 _right
       (write-word _right s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _left
     (setq _left (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _right
     (setq _right (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get pi_robot::Speed :md5sum-) "09d1b2323a1aeae9343e81809a820b60")
(setf (get pi_robot::Speed :datatype-) "pi_robot/Speed")
(setf (get pi_robot::Speed :definition-)
      "int16 left
int16 right

")



(provide :pi_robot/Speed "09d1b2323a1aeae9343e81809a820b60")


