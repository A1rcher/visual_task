; Auto-generated. Do not edit!


(cl:in-package demo01_action-msg)


;//! \htmlinclude addintsFeedback.msg.html

(cl:defclass <addintsFeedback> (roslisp-msg-protocol:ros-message)
  ((progress
    :reader progress
    :initarg :progress
    :type cl:float
    :initform 0.0))
)

(cl:defclass addintsFeedback (<addintsFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <addintsFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'addintsFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name demo01_action-msg:<addintsFeedback> is deprecated: use demo01_action-msg:addintsFeedback instead.")))

(cl:ensure-generic-function 'progress-val :lambda-list '(m))
(cl:defmethod progress-val ((m <addintsFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader demo01_action-msg:progress-val is deprecated.  Use demo01_action-msg:progress instead.")
  (progress m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <addintsFeedback>) ostream)
  "Serializes a message object of type '<addintsFeedback>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'progress))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <addintsFeedback>) istream)
  "Deserializes a message object of type '<addintsFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'progress) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<addintsFeedback>)))
  "Returns string type for a message object of type '<addintsFeedback>"
  "demo01_action/addintsFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'addintsFeedback)))
  "Returns string type for a message object of type 'addintsFeedback"
  "demo01_action/addintsFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<addintsFeedback>)))
  "Returns md5sum for a message object of type '<addintsFeedback>"
  "7afca0099e0cddc25243b1e3569895fe")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'addintsFeedback)))
  "Returns md5sum for a message object of type 'addintsFeedback"
  "7afca0099e0cddc25243b1e3569895fe")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<addintsFeedback>)))
  "Returns full string definition for message of type '<addintsFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%float64 progress~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'addintsFeedback)))
  "Returns full string definition for message of type 'addintsFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%float64 progress~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <addintsFeedback>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <addintsFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'addintsFeedback
    (cl:cons ':progress (progress msg))
))
