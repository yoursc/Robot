# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "pi_robot: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ipi_robot:/home/pi/catkin_ws/src/pi_robot/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pi_robot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_custom_target(_pi_robot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pi_robot" "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pi_robot
  "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pi_robot
)

### Generating Services

### Generating Module File
_generate_module_cpp(pi_robot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pi_robot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pi_robot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pi_robot_generate_messages pi_robot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_dependencies(pi_robot_generate_messages_cpp _pi_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pi_robot_gencpp)
add_dependencies(pi_robot_gencpp pi_robot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pi_robot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pi_robot
  "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pi_robot
)

### Generating Services

### Generating Module File
_generate_module_eus(pi_robot
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pi_robot
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pi_robot_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pi_robot_generate_messages pi_robot_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_dependencies(pi_robot_generate_messages_eus _pi_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pi_robot_geneus)
add_dependencies(pi_robot_geneus pi_robot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pi_robot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pi_robot
  "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pi_robot
)

### Generating Services

### Generating Module File
_generate_module_lisp(pi_robot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pi_robot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pi_robot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pi_robot_generate_messages pi_robot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_dependencies(pi_robot_generate_messages_lisp _pi_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pi_robot_genlisp)
add_dependencies(pi_robot_genlisp pi_robot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pi_robot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pi_robot
  "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pi_robot
)

### Generating Services

### Generating Module File
_generate_module_nodejs(pi_robot
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pi_robot
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pi_robot_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pi_robot_generate_messages pi_robot_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_dependencies(pi_robot_generate_messages_nodejs _pi_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pi_robot_gennodejs)
add_dependencies(pi_robot_gennodejs pi_robot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pi_robot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pi_robot
  "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pi_robot
)

### Generating Services

### Generating Module File
_generate_module_py(pi_robot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pi_robot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pi_robot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pi_robot_generate_messages pi_robot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/pi_robot/msg/Distance.msg" NAME_WE)
add_dependencies(pi_robot_generate_messages_py _pi_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pi_robot_genpy)
add_dependencies(pi_robot_genpy pi_robot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pi_robot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pi_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pi_robot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pi_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pi_robot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pi_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pi_robot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pi_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pi_robot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pi_robot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pi_robot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pi_robot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
