from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gt", type=str, default=r"D:\Dataset\coco\annotations/instances_val2017.json", help="Assign the groud true path.")
    parser.add_argument("-d", "--dt", type=str, default=r"D:\coding\YOLOv5\runs\val\val640/last_predictions.json",
                        help="Assign the detection result path.")
    args = parser.parse_args()

    cocoGt = COCO(args.gt)
    cocoDt = cocoGt.loadRes(args.dt)
    cocoEval = COCOeval(cocoGt, cocoDt, 'bbox')
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()
