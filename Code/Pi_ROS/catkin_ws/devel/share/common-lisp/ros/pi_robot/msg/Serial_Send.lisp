; Auto-generated. Do not edit!


(cl:in-package pi_robot-msg)


;//! \htmlinclude Serial_Send.msg.html

(cl:defclass <Serial_Send> (roslisp-msg-protocol:ros-message)
  ((info
    :reader info
    :initarg :info
    :type cl:string
    :initform ""))
)

(cl:defclass Serial_Send (<Serial_Send>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Serial_Send>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Serial_Send)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pi_robot-msg:<Serial_Send> is deprecated: use pi_robot-msg:Serial_Send instead.")))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <Serial_Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pi_robot-msg:info-val is deprecated.  Use pi_robot-msg:info instead.")
  (info m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Serial_Send>) ostream)
  "Serializes a message object of type '<Serial_Send>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'info))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Serial_Send>) istream)
  "Deserializes a message object of type '<Serial_Send>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'info) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'info) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Serial_Send>)))
  "Returns string type for a message object of type '<Serial_Send>"
  "pi_robot/Serial_Send")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Serial_Send)))
  "Returns string type for a message object of type 'Serial_Send"
  "pi_robot/Serial_Send")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Serial_Send>)))
  "Returns md5sum for a message object of type '<Serial_Send>"
  "c10fc26d5cca9a4b9114f5fc5dea9570")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Serial_Send)))
  "Returns md5sum for a message object of type 'Serial_Send"
  "c10fc26d5cca9a4b9114f5fc5dea9570")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Serial_Send>)))
  "Returns full string definition for message of type '<Serial_Send>"
  (cl:format cl:nil "string info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Serial_Send)))
  "Returns full string definition for message of type 'Serial_Send"
  (cl:format cl:nil "string info~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Serial_Send>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'info))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Serial_Send>))
  "Converts a ROS message object to a list"
  (cl:list 'Serial_Send
    (cl:cons ':info (info msg))
))
