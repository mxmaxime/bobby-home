from django.urls import include, path

from alarm.views.alarm_status_views import AlarmStatusList, AlarmStatusUpdate, AlarmStatusCreate, AlarmStatusSchedules, \
    AlarmScheduleUpdate, AlarmScheduleCreate
from camera.views.camera_motion_views import CameraMotionDetectedList, CameraMotionDetectedDetail
from camera.views.camera_roi_views import CameraROICreate, CameraROIUpdate, CameraROIList, CameraROIDelete
from camera.views.home import AlarmHome

app_name = 'alarm'

status_patterns = [
    path('', AlarmStatusList.as_view(), name='status-list'),
    path('<int:pk>/edit', AlarmStatusUpdate.as_view(), name='status-edit'),
    path('add', AlarmStatusCreate.as_view(), name='status-add'),
    path('<int:pk>/schedules', AlarmStatusSchedules.as_view(), name='status-schedules')
]


schedule_patterns = [
    path('<int:pk>/edit', AlarmScheduleUpdate.as_view(), name='schedule-edit'),
    path('add', AlarmScheduleCreate.as_view(), name='schedule-add')
]

roi_patterns = [
    path('', CameraROIList.as_view(), name='camera_roi-list'),
    path('<int:pk>/edit', CameraROIUpdate.as_view(), name='camera_roi-edit'),
    path('<int:pk>/delete', CameraROIDelete.as_view(), name='camera_roi-delete'),
    path('add', CameraROICreate.as_view(), name='camera_roi-add'),
]

motions_pattern = [
    path('', CameraMotionDetectedList.as_view(), name='camera_motion_detected-list'),
    path('<int:pk>', CameraMotionDetectedDetail.as_view(), name='camera_motion_detected-detail'),
]

urlpatterns = [
    path('', AlarmHome.as_view(), name='home'),
    path('status/', include(status_patterns)),
    path('schedule/', include(schedule_patterns)),
    path('camera_roi/', include(roi_patterns)),
    path('camera_motion/', include(motions_pattern)),
]
