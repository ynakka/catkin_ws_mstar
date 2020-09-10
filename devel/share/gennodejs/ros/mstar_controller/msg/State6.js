// Auto-generated. Do not edit!

// (in-package mstar_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class State6 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.state_x = null;
      this.state_y = null;
      this.state_theta = null;
      this.state_dx = null;
      this.state_dy = null;
      this.state_dtheta = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('state_x')) {
        this.state_x = initObj.state_x
      }
      else {
        this.state_x = 0.0;
      }
      if (initObj.hasOwnProperty('state_y')) {
        this.state_y = initObj.state_y
      }
      else {
        this.state_y = 0.0;
      }
      if (initObj.hasOwnProperty('state_theta')) {
        this.state_theta = initObj.state_theta
      }
      else {
        this.state_theta = 0.0;
      }
      if (initObj.hasOwnProperty('state_dx')) {
        this.state_dx = initObj.state_dx
      }
      else {
        this.state_dx = 0.0;
      }
      if (initObj.hasOwnProperty('state_dy')) {
        this.state_dy = initObj.state_dy
      }
      else {
        this.state_dy = 0.0;
      }
      if (initObj.hasOwnProperty('state_dtheta')) {
        this.state_dtheta = initObj.state_dtheta
      }
      else {
        this.state_dtheta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type State6
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [state_x]
    bufferOffset = _serializer.float32(obj.state_x, buffer, bufferOffset);
    // Serialize message field [state_y]
    bufferOffset = _serializer.float32(obj.state_y, buffer, bufferOffset);
    // Serialize message field [state_theta]
    bufferOffset = _serializer.float32(obj.state_theta, buffer, bufferOffset);
    // Serialize message field [state_dx]
    bufferOffset = _serializer.float32(obj.state_dx, buffer, bufferOffset);
    // Serialize message field [state_dy]
    bufferOffset = _serializer.float32(obj.state_dy, buffer, bufferOffset);
    // Serialize message field [state_dtheta]
    bufferOffset = _serializer.float32(obj.state_dtheta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type State6
    let len;
    let data = new State6(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [state_x]
    data.state_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_y]
    data.state_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_theta]
    data.state_theta = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_dx]
    data.state_dx = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_dy]
    data.state_dy = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_dtheta]
    data.state_dtheta = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mstar_controller/State6';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd8a965f0fe71dba3e08e4248ed66a1c0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new State6(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.state_x !== undefined) {
      resolved.state_x = msg.state_x;
    }
    else {
      resolved.state_x = 0.0
    }

    if (msg.state_y !== undefined) {
      resolved.state_y = msg.state_y;
    }
    else {
      resolved.state_y = 0.0
    }

    if (msg.state_theta !== undefined) {
      resolved.state_theta = msg.state_theta;
    }
    else {
      resolved.state_theta = 0.0
    }

    if (msg.state_dx !== undefined) {
      resolved.state_dx = msg.state_dx;
    }
    else {
      resolved.state_dx = 0.0
    }

    if (msg.state_dy !== undefined) {
      resolved.state_dy = msg.state_dy;
    }
    else {
      resolved.state_dy = 0.0
    }

    if (msg.state_dtheta !== undefined) {
      resolved.state_dtheta = msg.state_dtheta;
    }
    else {
      resolved.state_dtheta = 0.0
    }

    return resolved;
    }
};

module.exports = State6;
