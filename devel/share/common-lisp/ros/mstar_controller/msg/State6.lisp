; Auto-generated. Do not edit!


(cl:in-package mstar_controller-msg)


;//! \htmlinclude State6.msg.html

(cl:defclass <State6> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (state_x
    :reader state_x
    :initarg :state_x
    :type cl:float
    :initform 0.0)
   (state_y
    :reader state_y
    :initarg :state_y
    :type cl:float
    :initform 0.0)
   (state_theta
    :reader state_theta
    :initarg :state_theta
    :type cl:float
    :initform 0.0)
   (state_dx
    :reader state_dx
    :initarg :state_dx
    :type cl:float
    :initform 0.0)
   (state_dy
    :reader state_dy
    :initarg :state_dy
    :type cl:float
    :initform 0.0)
   (state_dtheta
    :reader state_dtheta
    :initarg :state_dtheta
    :type cl:float
    :initform 0.0))
)

(cl:defclass State6 (<State6>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <State6>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'State6)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mstar_controller-msg:<State6> is deprecated: use mstar_controller-msg:State6 instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:header-val is deprecated.  Use mstar_controller-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'state_x-val :lambda-list '(m))
(cl:defmethod state_x-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_x-val is deprecated.  Use mstar_controller-msg:state_x instead.")
  (state_x m))

(cl:ensure-generic-function 'state_y-val :lambda-list '(m))
(cl:defmethod state_y-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_y-val is deprecated.  Use mstar_controller-msg:state_y instead.")
  (state_y m))

(cl:ensure-generic-function 'state_theta-val :lambda-list '(m))
(cl:defmethod state_theta-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_theta-val is deprecated.  Use mstar_controller-msg:state_theta instead.")
  (state_theta m))

(cl:ensure-generic-function 'state_dx-val :lambda-list '(m))
(cl:defmethod state_dx-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_dx-val is deprecated.  Use mstar_controller-msg:state_dx instead.")
  (state_dx m))

(cl:ensure-generic-function 'state_dy-val :lambda-list '(m))
(cl:defmethod state_dy-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_dy-val is deprecated.  Use mstar_controller-msg:state_dy instead.")
  (state_dy m))

(cl:ensure-generic-function 'state_dtheta-val :lambda-list '(m))
(cl:defmethod state_dtheta-val ((m <State6>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mstar_controller-msg:state_dtheta-val is deprecated.  Use mstar_controller-msg:state_dtheta instead.")
  (state_dtheta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <State6>) ostream)
  "Serializes a message object of type '<State6>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_dx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_dy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state_dtheta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <State6>) istream)
  "Deserializes a message object of type '<State6>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_theta) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_dx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_dy) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state_dtheta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<State6>)))
  "Returns string type for a message object of type '<State6>"
  "mstar_controller/State6")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'State6)))
  "Returns string type for a message object of type 'State6"
  "mstar_controller/State6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<State6>)))
  "Returns md5sum for a message object of type '<State6>"
  "d8a965f0fe71dba3e08e4248ed66a1c0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'State6)))
  "Returns md5sum for a message object of type 'State6"
  "d8a965f0fe71dba3e08e4248ed66a1c0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<State6>)))
  "Returns full string definition for message of type '<State6>"
  (cl:format cl:nil "std_msgs/Header header~%float32 state_x~%float32 state_y~%float32 state_theta~%float32 state_dx~%float32 state_dy~%float32 state_dtheta~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'State6)))
  "Returns full string definition for message of type 'State6"
  (cl:format cl:nil "std_msgs/Header header~%float32 state_x~%float32 state_y~%float32 state_theta~%float32 state_dx~%float32 state_dy~%float32 state_dtheta~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <State6>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <State6>))
  "Converts a ROS message object to a list"
  (cl:list 'State6
    (cl:cons ':header (header msg))
    (cl:cons ':state_x (state_x msg))
    (cl:cons ':state_y (state_y msg))
    (cl:cons ':state_theta (state_theta msg))
    (cl:cons ':state_dx (state_dx msg))
    (cl:cons ':state_dy (state_dy msg))
    (cl:cons ':state_dtheta (state_dtheta msg))
))
