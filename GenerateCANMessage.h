//generated code by CANMessageParser

typedef union{
	uint8_t Txdata[8];
	uint8_t Rxdata[8];
	struct{
		uint16 defaultAngleLeft : 16;
		uint16 defaultAngleRight : 16;
		uint32 Remain : 32;
	}__attribute__((aligned(1),packed)) B;

}SV_set_t;

//generated code by CANMessageParser

typedef union{
	uint8_t Txdata[8];
	uint8_t Rxdata[8];
	struct{
		uint16 leftAngle : 16;
		uint16 rightAngle : 16;
		uint16 Roll : 16;
		uint16 heave : 16;
	}__attribute__((aligned(1),packed)) B;

}SV_calc_t;

