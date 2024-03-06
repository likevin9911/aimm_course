;; Auto-generated. Do not edit!


(when (boundp 'aimm_gazebo::BallShooter)
  (if (not (find-package "AIMM_GAZEBO"))
    (make-package "AIMM_GAZEBO"))
  (shadow 'BallShooter (find-package "AIMM_GAZEBO")))
(unless (find-package "AIMM_GAZEBO::BALLSHOOTER")
  (make-package "AIMM_GAZEBO::BALLSHOOTER"))
(unless (find-package "AIMM_GAZEBO::BALLSHOOTERREQUEST")
  (make-package "AIMM_GAZEBO::BALLSHOOTERREQUEST"))
(unless (find-package "AIMM_GAZEBO::BALLSHOOTERRESPONSE")
  (make-package "AIMM_GAZEBO::BALLSHOOTERRESPONSE"))

(in-package "ROS")





(defclass aimm_gazebo::BallShooterRequest
  :super ros::object
  :slots (_shoot ))

(defmethod aimm_gazebo::BallShooterRequest
  (:init
   (&key
    ((:shoot __shoot) nil)
    )
   (send-super :init)
   (setq _shoot __shoot)
   self)
  (:shoot
   (&optional (__shoot :null))
   (if (not (eq __shoot :null)) (setq _shoot __shoot)) _shoot)
  (:serialization-length
   ()
   (+
    ;; bool _shoot
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _shoot
       (if _shoot (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _shoot
     (setq _shoot (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass aimm_gazebo::BallShooterResponse
  :super ros::object
  :slots (_success ))

(defmethod aimm_gazebo::BallShooterResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass aimm_gazebo::BallShooter
  :super ros::object
  :slots ())

(setf (get aimm_gazebo::BallShooter :md5sum-) "e8e12124716653af3165b82608274851")
(setf (get aimm_gazebo::BallShooter :datatype-) "aimm_gazebo/BallShooter")
(setf (get aimm_gazebo::BallShooter :request) aimm_gazebo::BallShooterRequest)
(setf (get aimm_gazebo::BallShooter :response) aimm_gazebo::BallShooterResponse)

(defmethod aimm_gazebo::BallShooterRequest
  (:response () (instance aimm_gazebo::BallShooterResponse :init)))

(setf (get aimm_gazebo::BallShooterRequest :md5sum-) "e8e12124716653af3165b82608274851")
(setf (get aimm_gazebo::BallShooterRequest :datatype-) "aimm_gazebo/BallShooterRequest")
(setf (get aimm_gazebo::BallShooterRequest :definition-)
      "# Ball shooter service

bool shoot
---
bool success
")

(setf (get aimm_gazebo::BallShooterResponse :md5sum-) "e8e12124716653af3165b82608274851")
(setf (get aimm_gazebo::BallShooterResponse :datatype-) "aimm_gazebo/BallShooterResponse")
(setf (get aimm_gazebo::BallShooterResponse :definition-)
      "# Ball shooter service

bool shoot
---
bool success
")



(provide :aimm_gazebo/BallShooter "e8e12124716653af3165b82608274851")


