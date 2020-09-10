;; Auto-generated. Do not edit!


(when (boundp 'mstar_controller::Thrusters8)
  (if (not (find-package "MSTAR_CONTROLLER"))
    (make-package "MSTAR_CONTROLLER"))
  (shadow 'Thrusters8 (find-package "MSTAR_CONTROLLER")))
(unless (find-package "MSTAR_CONTROLLER::THRUSTERS8")
  (make-package "MSTAR_CONTROLLER::THRUSTERS8"))

(in-package "ROS")
;;//! \htmlinclude Thrusters8.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass mstar_controller::Thrusters8
  :super ros::object
  :slots (_header _FXpMZp _FXpMZm _FXmMZp _FXmMZm _FYpMZp _FYpMZm _FYmMZp _FYmMZm ))

(defmethod mstar_controller::Thrusters8
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:FXpMZp __FXpMZp) 0.0)
    ((:FXpMZm __FXpMZm) 0.0)
    ((:FXmMZp __FXmMZp) 0.0)
    ((:FXmMZm __FXmMZm) 0.0)
    ((:FYpMZp __FYpMZp) 0.0)
    ((:FYpMZm __FYpMZm) 0.0)
    ((:FYmMZp __FYmMZp) 0.0)
    ((:FYmMZm __FYmMZm) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _FXpMZp (float __FXpMZp))
   (setq _FXpMZm (float __FXpMZm))
   (setq _FXmMZp (float __FXmMZp))
   (setq _FXmMZm (float __FXmMZm))
   (setq _FYpMZp (float __FYpMZp))
   (setq _FYpMZm (float __FYpMZm))
   (setq _FYmMZp (float __FYmMZp))
   (setq _FYmMZm (float __FYmMZm))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:FXpMZp
   (&optional __FXpMZp)
   (if __FXpMZp (setq _FXpMZp __FXpMZp)) _FXpMZp)
  (:FXpMZm
   (&optional __FXpMZm)
   (if __FXpMZm (setq _FXpMZm __FXpMZm)) _FXpMZm)
  (:FXmMZp
   (&optional __FXmMZp)
   (if __FXmMZp (setq _FXmMZp __FXmMZp)) _FXmMZp)
  (:FXmMZm
   (&optional __FXmMZm)
   (if __FXmMZm (setq _FXmMZm __FXmMZm)) _FXmMZm)
  (:FYpMZp
   (&optional __FYpMZp)
   (if __FYpMZp (setq _FYpMZp __FYpMZp)) _FYpMZp)
  (:FYpMZm
   (&optional __FYpMZm)
   (if __FYpMZm (setq _FYpMZm __FYpMZm)) _FYpMZm)
  (:FYmMZp
   (&optional __FYmMZp)
   (if __FYmMZp (setq _FYmMZp __FYmMZp)) _FYmMZp)
  (:FYmMZm
   (&optional __FYmMZm)
   (if __FYmMZm (setq _FYmMZm __FYmMZm)) _FYmMZm)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _FXpMZp
    4
    ;; float32 _FXpMZm
    4
    ;; float32 _FXmMZp
    4
    ;; float32 _FXmMZm
    4
    ;; float32 _FYpMZp
    4
    ;; float32 _FYpMZm
    4
    ;; float32 _FYmMZp
    4
    ;; float32 _FYmMZm
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _FXpMZp
       (sys::poke _FXpMZp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FXpMZm
       (sys::poke _FXpMZm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FXmMZp
       (sys::poke _FXmMZp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FXmMZm
       (sys::poke _FXmMZm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FYpMZp
       (sys::poke _FYpMZp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FYpMZm
       (sys::poke _FYpMZm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FYmMZp
       (sys::poke _FYmMZp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _FYmMZm
       (sys::poke _FYmMZm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _FXpMZp
     (setq _FXpMZp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FXpMZm
     (setq _FXpMZm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FXmMZp
     (setq _FXmMZp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FXmMZm
     (setq _FXmMZm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FYpMZp
     (setq _FYpMZp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FYpMZm
     (setq _FYpMZm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FYmMZp
     (setq _FYmMZp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _FYmMZm
     (setq _FYmMZm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get mstar_controller::Thrusters8 :md5sum-) "51b0cb1b10c2fc8b58fb90e8108ac3ef")
(setf (get mstar_controller::Thrusters8 :datatype-) "mstar_controller/Thrusters8")
(setf (get mstar_controller::Thrusters8 :definition-)
      "std_msgs/Header header
float32 FXpMZp
float32 FXpMZm
float32 FXmMZp
float32 FXmMZm
float32 FYpMZp
float32 FYpMZm
float32 FYmMZp
float32 FYmMZm


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



(provide :mstar_controller/Thrusters8 "51b0cb1b10c2fc8b58fb90e8108ac3ef")


