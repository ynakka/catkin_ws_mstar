# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mstar_navigation: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imstar_navigation:/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mstar_navigation_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_custom_target(_mstar_navigation_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mstar_navigation" "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mstar_navigation
  "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mstar_navigation
)

### Generating Services

### Generating Module File
_generate_module_cpp(mstar_navigation
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mstar_navigation
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mstar_navigation_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mstar_navigation_generate_messages mstar_navigation_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_dependencies(mstar_navigation_generate_messages_cpp _mstar_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mstar_navigation_gencpp)
add_dependencies(mstar_navigation_gencpp mstar_navigation_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mstar_navigation_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(mstar_navigation
  "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mstar_navigation
)

### Generating Services

### Generating Module File
_generate_module_eus(mstar_navigation
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mstar_navigation
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(mstar_navigation_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(mstar_navigation_generate_messages mstar_navigation_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_dependencies(mstar_navigation_generate_messages_eus _mstar_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mstar_navigation_geneus)
add_dependencies(mstar_navigation_geneus mstar_navigation_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mstar_navigation_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mstar_navigation
  "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mstar_navigation
)

### Generating Services

### Generating Module File
_generate_module_lisp(mstar_navigation
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mstar_navigation
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mstar_navigation_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mstar_navigation_generate_messages mstar_navigation_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_dependencies(mstar_navigation_generate_messages_lisp _mstar_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mstar_navigation_genlisp)
add_dependencies(mstar_navigation_genlisp mstar_navigation_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mstar_navigation_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(mstar_navigation
  "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mstar_navigation
)

### Generating Services

### Generating Module File
_generate_module_nodejs(mstar_navigation
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mstar_navigation
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(mstar_navigation_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(mstar_navigation_generate_messages mstar_navigation_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_dependencies(mstar_navigation_generate_messages_nodejs _mstar_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mstar_navigation_gennodejs)
add_dependencies(mstar_navigation_gennodejs mstar_navigation_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mstar_navigation_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mstar_navigation
  "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mstar_navigation
)

### Generating Services

### Generating Module File
_generate_module_py(mstar_navigation
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mstar_navigation
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mstar_navigation_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mstar_navigation_generate_messages mstar_navigation_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/nvidia/catkin_ws_mstar/src/mstar_navigation/msg/State6.msg" NAME_WE)
add_dependencies(mstar_navigation_generate_messages_py _mstar_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mstar_navigation_genpy)
add_dependencies(mstar_navigation_genpy mstar_navigation_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mstar_navigation_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mstar_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mstar_navigation
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(mstar_navigation_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(mstar_navigation_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mstar_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mstar_navigation
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(mstar_navigation_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(mstar_navigation_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mstar_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mstar_navigation
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(mstar_navigation_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(mstar_navigation_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mstar_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mstar_navigation
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(mstar_navigation_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(mstar_navigation_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mstar_navigation)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mstar_navigation\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mstar_navigation
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(mstar_navigation_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(mstar_navigation_generate_messages_py geometry_msgs_generate_messages_py)
endif()
