;; Auto-generated. Do not edit!


(when (boundp 'pi_robot::Distance)
  (if (not (find-package "PI_ROBOT"))
    (make-package "PI_ROBOT"))
  (shadow 'Distance (find-package "PI_ROBOT")))
(unless (find-package "PI_ROBOT::DISTANCE")
  (make-package "PI_ROBOT::DISTANCE"))

(in-package "ROS")
;;//! \htmlinclude Distance.msg.html


(defclass pi_robot::Distance
  :super ros::object
  :slots (_front _left _right ))

(defmethod pi_robot::Distance
  (:init
   (&key
    ((:front __front) 0)
    ((:left __left) 0)
    ((:right __right) 0)
    )
   (send-super :init)
   (setq _front (round __front))
   (setq _left (round __left))
   (setq _right (round __right))
   self)
  (:front
   (&optional __front)
   (if __front (setq _front __front)) _front)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:serialization-length
   ()
   (+
    ;; int16 _front
    2
    ;; int16 _left
    2
    ;; int16 _right
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _front
       (write-word _front s)
     ;; int16 _left
       (write-word _left s)
     ;; int16 _right
       (write-word _right s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _front
     (setq _front (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _left
     (setq _left (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _right
     (setq _right (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get pi_robot::Distance :md5sum-) "145c935186550897a7e4b51128ea594e")
(setf (get pi_robot::Distance :datatype-) "pi_robot/Distance")
(setf (get pi_robot::Distance :definition-)
      "int16 front
int16 left
int16 right

")



(provide :pi_robot/Distance "145c935186550897a7e4b51128ea594e")


