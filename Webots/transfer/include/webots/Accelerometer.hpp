/*******************************************************************************************************/
/* Description:  Wrapper of the Accelerometer Webots API for the ROBOTIS OP2 real robot                  */
/*******************************************************************************************************/

#ifndef ACCELEROMETER_HPP
#define ACCELEROMETER_HPP

#include <webots/Robot.hpp>
#include <webots/Device.hpp>

namespace webots {
  class Accelerometer: public Device  {
    public:
                    Accelerometer(const std::string &name); //Use Robot::getAccelerometer() instead
      virtual      ~Accelerometer();

      virtual void  enable(int samplingPeriod);
      virtual void  disable();

      const double *getValues() const;
      int           getSamplingPeriod() const;

    private:
      double        mValues[3];
      void          setValues(const int *integerValues);

      friend int Robot::step(int duration);
  };
}

#endif // ACCELEROMETER_HPP
