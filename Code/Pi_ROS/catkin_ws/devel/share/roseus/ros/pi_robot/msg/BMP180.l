;; Auto-generated. Do not edit!


(when (boundp 'pi_robot::BMP180)
  (if (not (find-package "PI_ROBOT"))
    (make-package "PI_ROBOT"))
  (shadow 'BMP180 (find-package "PI_ROBOT")))
(unless (find-package "PI_ROBOT::BMP180")
  (make-package "PI_ROBOT::BMP180"))

(in-package "ROS")
;;//! \htmlinclude BMP180.msg.html


(defclass pi_robot::BMP180
  :super ros::object
  :slots (_temperature _pressure _altitude ))

(defmethod pi_robot::BMP180
  (:init
   (&key
    ((:temperature __temperature) 0.0)
    ((:pressure __pressure) 0.0)
    ((:altitude __altitude) 0.0)
    )
   (send-super :init)
   (setq _temperature (float __temperature))
   (setq _pressure (float __pressure))
   (setq _altitude (float __altitude))
   self)
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:pressure
   (&optional __pressure)
   (if __pressure (setq _pressure __pressure)) _pressure)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:serialization-length
   ()
   (+
    ;; float32 _temperature
    4
    ;; float32 _pressure
    4
    ;; float32 _altitude
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pressure
       (sys::poke _pressure (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pressure
     (setq _pressure (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _altitude
     (setq _altitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pi_robot::BMP180 :md5sum-) "657251609a9411407cf7245117d8b584")
(setf (get pi_robot::BMP180 :datatype-) "pi_robot/BMP180")
(setf (get pi_robot::BMP180 :definition-)
      "float32 temperature
float32 pressure
float32 altitude

")



(provide :pi_robot/BMP180 "657251609a9411407cf7245117d8b584")


