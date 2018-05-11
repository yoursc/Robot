; Auto-generated. Do not edit!


(cl:in-package pi_robot-msg)


;//! \htmlinclude BMP180.msg.html

(cl:defclass <BMP180> (roslisp-msg-protocol:ros-message)
  ((temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0))
)

(cl:defclass BMP180 (<BMP180>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BMP180>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BMP180)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pi_robot-msg:<BMP180> is deprecated: use pi_robot-msg:BMP180 instead.")))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <BMP180>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pi_robot-msg:temperature-val is deprecated.  Use pi_robot-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <BMP180>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pi_robot-msg:pressure-val is deprecated.  Use pi_robot-msg:pressure instead.")
  (pressure m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <BMP180>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pi_robot-msg:altitude-val is deprecated.  Use pi_robot-msg:altitude instead.")
  (altitude m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BMP180>) ostream)
  "Serializes a message object of type '<BMP180>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pressure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BMP180>) istream)
  "Deserializes a message object of type '<BMP180>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pressure) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BMP180>)))
  "Returns string type for a message object of type '<BMP180>"
  "pi_robot/BMP180")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BMP180)))
  "Returns string type for a message object of type 'BMP180"
  "pi_robot/BMP180")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BMP180>)))
  "Returns md5sum for a message object of type '<BMP180>"
  "657251609a9411407cf7245117d8b584")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BMP180)))
  "Returns md5sum for a message object of type 'BMP180"
  "657251609a9411407cf7245117d8b584")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BMP180>)))
  "Returns full string definition for message of type '<BMP180>"
  (cl:format cl:nil "float32 temperature~%float32 pressure~%float32 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BMP180)))
  "Returns full string definition for message of type 'BMP180"
  (cl:format cl:nil "float32 temperature~%float32 pressure~%float32 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BMP180>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BMP180>))
  "Converts a ROS message object to a list"
  (cl:list 'BMP180
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':pressure (pressure msg))
    (cl:cons ':altitude (altitude msg))
))
