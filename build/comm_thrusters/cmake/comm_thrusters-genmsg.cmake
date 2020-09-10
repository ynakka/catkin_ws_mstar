# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "comm_thrusters: 1 messages, 0 services")

set(MSG_I_FLAGS "-Icomm_thrusters:/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(comm_thrusters_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_custom_target(_comm_thrusters_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "comm_thrusters" "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(comm_thrusters
  "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/comm_thrusters
)

### Generating Services

### Generating Module File
_generate_module_cpp(comm_thrusters
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/comm_thrusters
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(comm_thrusters_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(comm_thrusters_generate_messages comm_thrusters_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_dependencies(comm_thrusters_generate_messages_cpp _comm_thrusters_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(comm_thrusters_gencpp)
add_dependencies(comm_thrusters_gencpp comm_thrusters_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS comm_thrusters_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(comm_thrusters
  "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/comm_thrusters
)

### Generating Services

### Generating Module File
_generate_module_eus(comm_thrusters
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/comm_thrusters
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(comm_thrusters_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(comm_thrusters_generate_messages comm_thrusters_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_dependencies(comm_thrusters_generate_messages_eus _comm_thrusters_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(comm_thrusters_geneus)
add_dependencies(comm_thrusters_geneus comm_thrusters_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS comm_thrusters_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(comm_thrusters
  "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/comm_thrusters
)

### Generating Services

### Generating Module File
_generate_module_lisp(comm_thrusters
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/comm_thrusters
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(comm_thrusters_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(comm_thrusters_generate_messages comm_thrusters_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_dependencies(comm_thrusters_generate_messages_lisp _comm_thrusters_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(comm_thrusters_genlisp)
add_dependencies(comm_thrusters_genlisp comm_thrusters_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS comm_thrusters_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(comm_thrusters
  "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/comm_thrusters
)

### Generating Services

### Generating Module File
_generate_module_nodejs(comm_thrusters
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/comm_thrusters
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(comm_thrusters_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(comm_thrusters_generate_messages comm_thrusters_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_dependencies(comm_thrusters_generate_messages_nodejs _comm_thrusters_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(comm_thrusters_gennodejs)
add_dependencies(comm_thrusters_gennodejs comm_thrusters_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS comm_thrusters_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(comm_thrusters
  "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/comm_thrusters
)

### Generating Services

### Generating Module File
_generate_module_py(comm_thrusters
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/comm_thrusters
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(comm_thrusters_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(comm_thrusters_generate_messages comm_thrusters_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/comm_thrusters/msg/Thrusters8.msg" NAME_WE)
add_dependencies(comm_thrusters_generate_messages_py _comm_thrusters_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(comm_thrusters_genpy)
add_dependencies(comm_thrusters_genpy comm_thrusters_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS comm_thrusters_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/comm_thrusters)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/comm_thrusters
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(comm_thrusters_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/comm_thrusters)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/comm_thrusters
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(comm_thrusters_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/comm_thrusters)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/comm_thrusters
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(comm_thrusters_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/comm_thrusters)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/comm_thrusters
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(comm_thrusters_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/comm_thrusters)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/comm_thrusters\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/comm_thrusters
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(comm_thrusters_generate_messages_py std_msgs_generate_messages_py)
endif()
