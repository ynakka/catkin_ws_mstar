;; Auto-generated. Do not edit!


(when (boundp 'mstar_controller::State6)
  (if (not (find-package "MSTAR_CONTROLLER"))
    (make-package "MSTAR_CONTROLLER"))
  (shadow 'State6 (find-package "MSTAR_CONTROLLER")))
(unless (find-package "MSTAR_CONTROLLER::STATE6")
  (make-package "MSTAR_CONTROLLER::STATE6"))

(in-package "ROS")
;;//! \htmlinclude State6.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass mstar_controller::State6
  :super ros::object
  :slots (_header _state_x _state_y _state_theta _state_dx _state_dy _state_dtheta ))

(defmethod mstar_controller::State6
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:state_x __state_x) 0.0)
    ((:state_y __state_y) 0.0)
    ((:state_theta __state_theta) 0.0)
    ((:state_dx __state_dx) 0.0)
    ((:state_dy __state_dy) 0.0)
    ((:state_dtheta __state_dtheta) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _state_x (float __state_x))
   (setq _state_y (float __state_y))
   (setq _state_theta (float __state_theta))
   (setq _state_dx (float __state_dx))
   (setq _state_dy (float __state_dy))
   (setq _state_dtheta (float __state_dtheta))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:state_x
   (&optional __state_x)
   (if __state_x (setq _state_x __state_x)) _state_x)
  (:state_y
   (&optional __state_y)
   (if __state_y (setq _state_y __state_y)) _state_y)
  (:state_theta
   (&optional __state_theta)
   (if __state_theta (setq _state_theta __state_theta)) _state_theta)
  (:state_dx
   (&optional __state_dx)
   (if __state_dx (setq _state_dx __state_dx)) _state_dx)
  (:state_dy
   (&optional __state_dy)
   (if __state_dy (setq _state_dy __state_dy)) _state_dy)
  (:state_dtheta
   (&optional __state_dtheta)
   (if __state_dtheta (setq _state_dtheta __state_dtheta)) _state_dtheta)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _state_x
    4
    ;; float32 _state_y
    4
    ;; float32 _state_theta
    4
    ;; float32 _state_dx
    4
    ;; float32 _state_dy
    4
    ;; float32 _state_dtheta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _state_x
       (sys::poke _state_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _state_y
       (sys::poke _state_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _state_theta
       (sys::poke _state_theta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _state_dx
       (sys::poke _state_dx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _state_dy
       (sys::poke _state_dy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _state_dtheta
       (sys::poke _state_dtheta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _state_x
     (setq _state_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _state_y
     (setq _state_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _state_theta
     (setq _state_theta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _state_dx
     (setq _state_dx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _state_dy
     (setq _state_dy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _state_dtheta
     (setq _state_dtheta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get mstar_controller::State6 :md5sum-) "d8a965f0fe71dba3e08e4248ed66a1c0")
(setf (get mstar_controller::State6 :datatype-) "mstar_controller/State6")
(setf (get mstar_controller::State6 :definition-)
      "std_msgs/Header header
float32 state_x
float32 state_y
float32 state_theta
float32 state_dx
float32 state_dy
float32 state_dtheta
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :mstar_controller/State6 "d8a965f0fe71dba3e08e4248ed66a1c0")


