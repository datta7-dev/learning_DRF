from rest_framework import serializers
from mainapi.models import Student


""" class studentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    marks = serializers.IntegerField()


# validators,user_defined
def check_marks(value):
    if value > 100:
        raise serializers.ValidationError("marks out of range")


class postStudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    marks = serializers.IntegerField(validators=[check_marks])

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    # field level validation
    def validate_roll_no(self, rn):
        if rn >= 100:
            raise serializers.ValidationError("roll number out of range")
        return rn

    # object level validation, parameter gives us data in the form of dictionary
    def validate(self, data):
        rn = data.get('roll_no')
        name = data.get('name')
        marks = data.get('marks')

        if marks <= 39:
            raise serializers.ValidationError("student failed")
        return data


class getStudentDataSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    marks = serializers.IntegerField()


class updateStudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    marks = serializers.IntegerField()

    def update(self, obj, validate_data):
        obj.roll_no = validate_data.get('roll_no', obj.roll_no)
        obj.name = validate_data.get('name', obj.name)
        obj.marks = validate_data.get('marks', obj.marks)
        obj.save()
        return obj
 """


# model serializer, it automatically generates sertializer class by default.
class studentSerializer(serializers.ModelSerializer):
    # roll_no = serializers.IntegerField(read_only=True) #to make field as a read only
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student  # model name
        # fields which we need to be work with in serialization
        fields = ['roll_no', 'name', 'marks']
        # fields = '__all__'  # for all fields in serialization
        # another way to make field as a read only
        read_only_fields = ['roll_no', 'name']
        #validators=[]
