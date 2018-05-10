;; Auto-generated. Do not edit!


(when (boundp 'pi_robot::Serial_Send)
  (if (not (find-package "PI_ROBOT"))
    (make-package "PI_ROBOT"))
  (shadow 'Serial_Send (find-package "PI_ROBOT")))
(unless (find-package "PI_ROBOT::SERIAL_SEND")
  (make-package "PI_ROBOT::SERIAL_SEND"))

(in-package "ROS")
;;//! \htmlinclude Serial_Send.msg.html


(defclass pi_robot::Serial_Send
  :super ros::object
  :slots (_info ))

(defmethod pi_robot::Serial_Send
  (:init
   (&key
    ((:info __info) "")
    )
   (send-super :init)
   (setq _info (string __info))
   self)
  (:info
   (&optional __info)
   (if __info (setq _info __info)) _info)
  (:serialization-length
   ()
   (+
    ;; string _info
    4 (length _info)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _info
       (write-long (length _info) s) (princ _info s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _info
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _info (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get pi_robot::Serial_Send :md5sum-) "c10fc26d5cca9a4b9114f5fc5dea9570")
(setf (get pi_robot::Serial_Send :datatype-) "pi_robot/Serial_Send")
(setf (get pi_robot::Serial_Send :definition-)
      "string info

")



(provide :pi_robot/Serial_Send "c10fc26d5cca9a4b9114f5fc5dea9570")


