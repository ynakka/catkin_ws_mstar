
(cl:in-package :asdf)

(defsystem "mstar_navigation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "State6" :depends-on ("_package_State6"))
    (:file "_package_State6" :depends-on ("_package"))
  ))