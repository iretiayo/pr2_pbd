''' Robot speech'''
import roslib
roslib.load_manifest('pr2_pbd_interaction')
import rospy
from sound_play.msg import SoundRequest
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA


class RobotSpeech:
    '''The robot's speech responses.'''
    # General
    TEST_RESPONSE = 'Microphone working.'

    # Creating/moving around actions
    SKILL_CREATED = 'Created action'
    SWITCH_SKILL = 'Switched to action'
    ERROR_NEXT_SKILL = 'No actions after action'
    ERROR_PREV_SKILL = 'No actions before action'
    ERROR_NO_SKILLS = 'No actions created yet.'

    # Relax / freeze arms
    RIGHT_ARM_RELEASED = 'Right arm relaxed'
    RIGHT_ARM_HOLDING = 'Right arm frozen'
    LEFT_ARM_RELEASED = 'Left arm relaxed'
    LEFT_ARM_HOLDING = 'Left arm frozen'
    RIGHT_ARM_ALREADY_HOLDING = 'Right arm is already frozen.'
    RIGHT_ARM_ALREADY_RELEASED = 'Right arm is already relaxed.'
    LEFT_ARM_ALREADY_HOLDING = 'Left arm is already frozen.'
    LEFT_ARM_ALREADY_RELEASED = 'Left arm is already relaxed.'

    # Open/close hands
    RIGHT_HAND_OPENING = 'Opening right hand'
    RIGHT_HAND_CLOSING = 'Closing right hand'
    LEFT_HAND_OPENING = 'Opening left hand'
    LEFT_HAND_CLOSING = 'Closing left hand'
    RIGHT_HAND_ALREADY_OPEN = 'Right hand is already open.'
    RIGHT_HAND_ALREADY_CLOSED = 'Right hand is already closed.'
    LEFT_HAND_ALREADY_OPEN = 'Left hand is already open.'
    LEFT_HAND_ALREADY_CLOSED = 'Left hand is already closed.'

    # Recording object poses
    START_STATE_RECORDED = 'Start state recorded.'
    OBJECT_NOT_DETECTED = 'No objects were detected.'

    # Mucking with steps (poses).
    STEP_RECORDED = 'Pose saved.'
    SKILL_EMPTY = 'Action has no poses to delete.'
    LAST_POSE_DELETED = 'Last pose deleted.'
    SKILL_CLEARED = 'All poses deleted.'

    # Executing
    START_EXECUTION = 'Starting execution of action'
    EXECUTION_ENDED = 'Execution ended'
    ERROR_NO_EXECUTION = 'No executions in progress.'
    EXECUTION_PREEMPTED = 'Stopping execution.'
    STOPPING_EXECUTION = 'Execution stopped.'
    EXECUTION_ERROR_NOIK = 'Cannot execute action'
    EXECUTION_ERROR_NOPOSES = 'Not enough poses in action'

    # Trajectories
    STARTED_RECORDING_MOTION = 'Started recording motion.'
    STOPPED_RECORDING_MOTION = 'Stopped recording motion.'
    MOTION_NOT_RECORDING = 'Not currently recording motion.'
    ALREADY_RECORDING_MOTION = 'Already recording motion.'

    # TODO(mbforbes): Remove the following as they're currently
    # impossible to reach.
    POSE_DELETED = 'Last pose deleted'
    ALL_POSES_RESUMED = 'All poses resumed.'
    POSE_RESUMED = 'Pose resumed'
    DELETED_SKILL = 'Deleted action'
    ACTION_ALREADY_STARTED = (
        'Action already started. Say, delete all steps, to start over.')

    def __init__(self):
        self.speech_publisher = rospy.Publisher('robotsound', SoundRequest)
        self.marker_publisher = rospy.Publisher('visualization_marker', Marker)

    def say(self, text, is_using_sounds=False):
        ''' Send a TTS command'''
        if (not is_using_sounds):
            self.speech_publisher.publish(SoundRequest(
                                        command=SoundRequest.SAY, arg=text))
        self.say_in_rviz(text)

    def say_in_rviz(self, text):
        ''' Visualizes the text that is uttered by the robot in rviz'''
        marker = Marker(type=Marker.TEXT_VIEW_FACING, id=1000,
                   lifetime=rospy.Duration(1.5),
                   pose=Pose(Point(0.5, 0.5, 1.45), Quaternion(0, 0, 0, 1)),
                   scale=Vector3(0.06, 0.06, 0.06),
                   header=Header(frame_id='base_link'),
                   color=ColorRGBA(0.0, 1.0, 0.0, 0.8), text=text)
        self.marker_publisher.publish(marker)
